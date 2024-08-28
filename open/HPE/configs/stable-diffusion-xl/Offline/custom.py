# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_L40S_PCIe_48GBx4(L40Sx1):
    system = KnownSystem.HPE_ProLiant_DL380a_L40S_PCIe_48GBx4
    gpu_batch_size = {'clip1': 1 * 2, 'clip2': 1 * 2, 'unet': 1 * 2, 'vae': 1}
    offline_expected_qps = 0.6*4
    use_graphs = True
    precision = "fp8"

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_H100_PCIe_80GBx4(OfflineGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_H100_PCIe_80GBx4
    gpu_batch_size = {'clip1': 8 * 2, 'clip2': 8 * 2, 'unet': 8 * 2, 'vae': 8}
    precision = "int8"
    gpu_inference_streams = 1
    gpu_copy_streams = 1
    offline_expected_qps = 4
    use_graphs = False #True

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H100_NVL_94GBX4(OfflineGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_H100_NVL_94GBx4
    gpu_batch_size = {'clip1': 8 * 2, 'clip2': 8 * 2, 'unet': 8 * 2, 'vae': 8}
    precision = "fp8" #"int8"
    use_graphs = False #True
    gpu_inference_streams = 1
    gpu_copy_streams = 1
    offline_expected_qps = 6

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_CRAY_XD670_H100_SXM_80GBX8(H100_SXM_80GBx8):
    system = KnownSystem.HPE_Cray_XD670_H100_SXM_80GBx8
    gpu_batch_size = {'clip1': 8 * 2, 'clip2': 8 * 2, 'unet': 8 * 2, 'vae': 8}
    offline_expected_qps = 17.5 #17 #18 #16 #15 #14 #13.2
    use_graphs = True
    start_from_device = True
    gpu_inference_streams = 4 #2 #4 <<<new

"""     # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):

    # Optional fields:
    active_sms: int = 0
    buffer_manager_thread_count: int = 0
    cache_file: str = ''
    gpu_copy_streams: int = 0
    gpu_inference_streams: int = 0
    instance_group_count: int = 0
    model_path: str = ''
    numa_config: str = ''
    offline_expected_qps: float = 0.0
    performance_sample_count_override: int = 0
    preferred_batch_size: str = ''
    request_timeout_usec: int = 0
    run_infer_on_copy_streams: bool = False
    use_graphs: bool = False
    use_jemalloc: bool = False
    use_spin_wait: bool = False
    verbose_glog: int = 0
    workspace_size: int = 0 """



