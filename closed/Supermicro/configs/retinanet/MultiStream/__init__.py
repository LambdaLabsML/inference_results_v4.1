# Copyright (c) 2024, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
sys.path.insert(0, os.getcwd())

from importlib import import_module
from code.common.constants import Benchmark, Scenario
from code.common.systems.system_list import KnownSystem
from configs.configuration import *


GPUBaseConfig = import_module("configs.retinanet").GPUBaseConfig


class MultiStreamGPUBaseConfig(GPUBaseConfig):
    scenario = Scenario.MultiStream
    gpu_batch_size = {'retinanet': 8}
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    multi_stream_samples_per_query = 8
    multi_stream_target_latency_percentile = 99
    use_graphs = True
    disable_beta1_smallk = True


class GH200_96GB_aarch64x1(MultiStreamGPUBaseConfig):
    multi_stream_expected_latency_ns = 7000000


class L4x1(MultiStreamGPUBaseConfig):
    multi_stream_expected_latency_ns = 40000000


class L40x1(MultiStreamGPUBaseConfig):
    multi_stream_expected_latency_ns = 12000000


class H100_SXM_80GBx1(MultiStreamGPUBaseConfig):
    multi_stream_expected_latency_ns = 7000000


class H100_SXM_80GBx1_Triton(H100_SXM_80GBx1):
    use_triton = True


class H100_PCIe_80GBx1(MultiStreamGPUBaseConfig):
    multi_stream_expected_latency_ns = 10000000


class H100_PCIe_80GBx1_Triton(H100_PCIe_80GBx1):
    use_triton = True


class H100_PCIe_80GB_aarch64x1(MultiStreamGPUBaseConfig):
    multi_stream_expected_latency_ns = 12000000


class A100_PCIe_80GBx1(MultiStreamGPUBaseConfig):
    multi_stream_expected_latency_ns = 12000000


class A100_PCIe_80GBx1_Triton(A100_PCIe_80GBx1):
    use_triton = True


class A100_SXM_80GBx1(MultiStreamGPUBaseConfig):
    start_from_device = True
    multi_stream_expected_latency_ns = 9000000


class A100_SXM_80GBx1_Triton(A100_SXM_80GBx1):
    use_triton = True


class A100_SXM_80GB_MIG_1x1g10gb(MultiStreamGPUBaseConfig):
    start_from_device = True
    multi_stream_expected_latency_ns = 62000000
    # Use early stopping estimate due to long runtime.
    min_duration = 3600000
    min_query_count = 45000


class A100_SXM_80GB_MIG_1x1g10gb_Triton(A100_SXM_80GB_MIG_1x1g10gb):
    use_triton = True


class A2x1(MultiStreamGPUBaseConfig):
    multi_stream_expected_latency_ns = 114000000
    # Use early stopping estimate due to long runtime.
    min_duration = 3600000
    min_query_count = 16384


class A2x1_Triton(A2x1):
    use_triton = True
    multi_stream_expected_latency_ns = 114100000


class Orin(MultiStreamGPUBaseConfig):
    workspace_size = 30000000000
    multi_stream_expected_latency_ns = 130000000
    gpu_copy_streams = 2
    use_direct_host_access = True
    gpu_batch_size = {'retinanet': 2}

    # Use early stopping estimate due to long runtime.
    min_duration = 3600000
    min_query_count = 20000


class Orin_Triton(Orin):
    use_triton = True


class Orin_MaxQ(Orin):
    soc_cpu_freq = 576000
    soc_gpu_freq = 714000000
    soc_dla_freq = 0
    soc_emc_freq = 2133000000
    soc_pva_freq = 115000000
    orin_num_cores = 4
    multi_stream_expected_latency_ns = 184064122


class Orin_NX(MultiStreamGPUBaseConfig):
    workspace_size = 30000000000
    multi_stream_expected_latency_ns = 330000000
    gpu_copy_streams = 2
    use_direct_host_access = True
    gpu_batch_size = {'retinanet': 2}

    # Use early stopping estimate due to long runtime.
    min_duration = 3600000
    min_query_count = 8000


class Orin_NX_MaxQ(Orin_NX):
    soc_cpu_freq = 576000
    soc_gpu_freq = 828750000
    soc_dla_freq = 0
    soc_emc_freq = 2133000000
    soc_pva_freq = 115000000
    orin_num_cores = 4
    multi_stream_expected_latency_ns = 330000000
