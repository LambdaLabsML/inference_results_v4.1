import random
from transformers import AutoModelForCausalLM, AutoTokenizer
from torch.nn.utils.rnn import pad_sequence
import torch.nn.functional as F
from datasets import load_from_disk
from item import OutputItem
import torch
import numpy as np
import logging
import json
import copy

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("DATASET")


# TODO: Remove this before submissoin
USE_RANDOM = True
if USE_RANDOM:
    random.seed(9973)


Buckets = dict()
cutoff_step = 64
min_cutoff = 64
min_len = 1
for cutoff in range(min_cutoff, 1921, cutoff_step):  # All input sequences
    Buckets[cutoff] = list(range(min_len, cutoff, 1))
    min_len = cutoff

INPUT_BUCKETS = dict()
for cutoff, seq_lens in Buckets.items():
    for seq_len in seq_lens:
        INPUT_BUCKETS[seq_len] = cutoff

MAX_SAMPLES = 13368  # maximum samples available in the dataset
IGNORE_INDEX = -100
DEFAULT_PAD_TOKEN = "[PAD]"
DEFAULT_EOS_TOKEN = "</s>"
DEFAULT_BOS_TOKEN = "</s>"
DEFAULT_UNK_TOKEN = "</s>"
PROMPT_DICT = {
    "prompt_input": (
        "Below is an instruction that describes a task, paired with an input that provides further context. "
        "Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:"
    ),
    "prompt_no_input": (
        "Below is an instruction that describes a task. "
        "Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n{instruction}\n\n### Response:"
    ),
}

input_buckets = dict()

for cutoff, seq_lens in Buckets.items():
    for seq_len in seq_lens:
        input_buckets[seq_len] = cutoff  # min(cutoff,1919) # Max bucket length should be 1919


class Dataset(object):
    """ Dataset class for gpt-j """

    def __init__(self, dataset_path=None, model_checkpoint_path="EleutherAI/gpt-j-6B", total_sample_count=MAX_SAMPLES, pad_inputs=False):
        self.dataset_path = dataset_path

        self.tokenizer = AutoTokenizer.from_pretrained(model_checkpoint_path,
                                                       model_max_length=2048,
                                                       padding_side="left",
                                                       use_fast=False,)

        self.total_sample_count = total_sample_count
        self.pad_inputs = pad_inputs

    def loadDataset(self):
        """ Loads the dataset into memory """

        with open(self.dataset_path, "r") as fid:
            list_data_dict = json.load(fid)
            self.list_data_dict = copy.deepcopy(list_data_dict)

            self.total_sample_count = min(self.total_sample_count, len(list_data_dict))

            if USE_RANDOM:  # TODO: Remove this before submission
                list_data_dict = random.choices(list_data_dict, k=self.total_sample_count)

        prompt_input, prompt_no_input = PROMPT_DICT["prompt_input"], PROMPT_DICT["prompt_no_input"]
        self.dataset = []
        for example in list_data_dict:  # [:self.total_sample_count]:
            source = prompt_input.format_map(example)
            input_sample = self.tokenize_function(source)
            input_ids = input_sample.input_ids[0]
            input_len = len(input_ids)
            attn_mask = None
            if self.pad_inputs:
                len_bucket = input_buckets[input_len]
                pad_size = len_bucket - input_len
                input_len = len_bucket
                pad_tup = (pad_size, 0)  # Do left padding
                input_ids = F.pad(input_ids, pad=pad_tup, value=self.tokenizer.pad_token_id)
                attn_mask = F.pad(attn_mask, pad=pad_tup)
            self.dataset.append((input_ids, input_len, attn_mask))

        self.targets = [f"{example['output']}" for example in list_data_dict]

    def getWarmupSamples(self):
        """ Loads samples to use for warmup """

        cutoff_set = set(range(128, 1921, 256))
        warmup_samples = []

        prompt_input, prompt_no_input = PROMPT_DICT["prompt_input"], PROMPT_DICT["prompt_no_input"]
        sources = [prompt_input.format_map(example) for example in self.list_data_dict]

        for source in sources:  # input_ids, input_len, attn_mask in self.dataset:
            tok_input = self.tokenize_function(source)
            input_ids = tok_input.input_ids[0]
            input_len = len(input_ids)
            bucket = INPUT_BUCKETS[input_len]
            if bucket in cutoff_set:
                attn_mask = torch.ones(input_len).reshape((1, input_len))
                # TODO: pad value should be from tokenizer
                if self.pad_inputs:
                    pad_size = bucket - input_len
                    pad_tup = (pad_size, 0)
                    input_ids = F.pad(input_ids, pad=pad_tup, value=self.tokenizer.pad_token_id)
                    attn_mask = F.pad(attn_mask, pad=pad_tup)
                warmup_samples.append((input_ids, input_ids.shape[-1], attn_mask))

                cutoff_set.remove(bucket)
                if len(cutoff_set) == 0:
                    break
        return warmup_samples

    @torch.no_grad()
    def tokenize_function(self, examples):
        return self.tokenizer([examples], truncation=True, max_length=1919, return_tensors=None, padding=False)

    def postProcess(self, query_id_list, sample_index_list, out_tokens, input_seq_lens):
        """ Postprocesses the predicted output
             output:    .output_tokens tensor
                        .input_seq_lens
        """

        # TODO: Move this to backend?
        preds = []
        for i in range(out_tokens.shape[0]):
            query_id = query_id_list[i]         # TODO: Remove (not used)
            sample_index = sample_index_list[i]  # TODO: Remove (not needed)
            input_len = input_seq_lens[i]
            pred = out_tokens[i, input_len:].reshape(-1).cpu().numpy()  # TODO: For bs>1, need to check this slicing
            preds.append(pred)

        return OutputItem(query_id_list, preds)

    def __getitem__(self, index):
        """ Returns sample at 'index' """
        return self.dataset[index]

    def __len__(self):
        return len(self.dataset)

    @torch.no_grad()
    def getSamples(self, sample_index_list):
        """ Returns samples given 'sample_index_list' """
        return (
            [self.dataset[i][0] for i in sample_index_list],  # input_ids
            [self.dataset[i][1] for i in sample_index_list],  # length
            [None for i in sample_index_list],  # no mask needed
        )

    @torch.no_grad()
    def collate_batch(self, batch):

        input_ids_padded = []
        last_ind = []
        past_key_values = []
        attention_mask_padded = []
        position_ids_padded = []

        for input_ids, original_len, input_lens in batch:
            pad_len = input_ids.shape[-1] - original_len
            last_ind.append(original_len - 1)
            attention_mask = torch.ones(original_len).view(1, -1)

            attention_mask = torch.ones(original_len).view(1, -1)

            position_ids = torch.arange(original_len).view(1, -1)

            input_ids_padded.append(input_ids)
            attention_mask_padded.append(attention_mask)
            position_ids_padded.append(position_ids)

            beam_idx_tmp = torch.zeros((2048, int(4)), dtype=torch.long).contiguous()
            past_key_value = [
                (torch.zeros([1, 16, 1, 256]).contiguous(), torch.zeros([1, 16, 1, 256]).contiguous(),
                 beam_idx_tmp, torch.zeros(1, dtype=torch.long).contiguous())
                for i in range(28)
            ]

        return (
            (
                torch.vstack(input_ids_padded),
                tuple(past_key_value),
                torch.vstack(position_ids_padded),
                torch.vstack(attention_mask_padded),
            ),
            torch.tensor(last_ind),
        )
