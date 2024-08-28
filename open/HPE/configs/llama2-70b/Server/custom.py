# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_L40S_PCIe_48GBx4(ServerGPUBaseConfig):
    server_target_qps = 16.7*4
    system = KnownSystem.HPE_ProLiant_DL380a_L40S_PCIe_48GBx4
    gpu_batch_size = {'llama2-70b': 256}
    use_fp8 = True
    enable_sort = False

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_L40S_PCIe_48GBx4_HighAccuracy(HPE_ProLiant_DL380a_L40S_PCIe_48GBx4):
    pass

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_H100_PCIe_80GBx4(ServerGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_H100_PCIe_80GBx4
    server_target_qps = 5*4
    gpu_batch_size = {'llama2-70b': 1024}
    kvcache_free_gpu_mem_frac = 0.95 #0.90
    use_fp8 = True
    enable_sort = False
    tensor_parallelism = 2

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_H100_PCIe_80GBx4_HighAccuracy(HPE_ProLiant_DL380a_H100_PCIe_80GBx4):
    pass

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H100_NVL_94GBX4(H100_NVL_94GB_TP2x2):
    system = KnownSystem.HPE_ProLiant_DL380a_H100_NVL_94GBx4
    server_target_qps = 14*2
    gpu_batch_size = {'llama2-70b': 1024}
    kvcache_free_gpu_mem_frac = 0.95 #0.90
    use_fp8 = True
    enable_sort = False
    tensor_parallelism = 2
    vboost_slider = 1

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H100_NVL_94GBX4_HighAccuracy(HPE_PROLIANT_DL380A_H100_NVL_94GBX4):
    pass

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_CRAY_XD670_H100_SXM_80GBX8(H100_SXM_80GB_TP2x4):
    system = KnownSystem.HPE_Cray_XD670_H100_SXM_80GBx8
    server_target_qps = 80
    gpu_batch_size = {'llama2-70b': 1024}
    kvcache_free_gpu_mem_frac = 0.97 #0.90
    use_fp8 = True
    #enable_sort = False
    #tensor_parallelism = 2
    #vboost_slider = 1

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_CRAY_XD670_H100_SXM_80GBX8_HighAccuracy(HPE_CRAY_XD670_H100_SXM_80GBX8):
    server_target_qps = 80 #20 * 4 #66 #13.5 * 4  #63
    gpu_batch_size = {'llama2-70b': 1024}
    kvcache_free_gpu_mem_frac = 0.97 #0.90
    use_fp8 = True
    pass

"""     # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):

    # Optional fields:
    active_sms: int = 0
    buffer_manager_thread_count: int = 0
    cache_file: str = ''
    coalesced_tensor: bool = False
    enable_sort: bool = False
    gpu_copy_streams: int = 0
    gpu_inference_streams: int = 0
    gpu_rank_map: str = ''
    instance_group_count: int = 0
    kvcache_free_gpu_mem_frac: float = 0.0
    llm_gen_config_path: str = ''
    max_num_tokens: int = 0
    model_path: str = ''
    num_sort_segments: int = 0
    numa_config: str = ''
    performance_sample_count_override: int = 0
    pipeline_parallelism: int = 0
    preferred_batch_size: str = ''
    request_timeout_usec: int = 0
    run_infer_on_copy_streams: bool = False
    schedule_rng_seed: int = 0
    server_num_issue_query_threads: int = 0
    server_target_latency_ns: int = 0
    server_target_latency_percentile: float = 0.0
    server_target_qps: int = 0
    server_target_qps_adj_factor: float = 0.0
    tensor_parallelism: int = 0
    use_fp8: bool = False
    use_graphs: bool = False
    use_jemalloc: bool = False
    use_spin_wait: bool = False
    use_token_latencies: bool = False
    verbose_glog: int = 0
    workspace_size: int = 0
 """
