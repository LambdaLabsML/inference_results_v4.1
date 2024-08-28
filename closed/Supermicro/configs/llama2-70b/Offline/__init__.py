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

ParentConfig = import_module("configs.llama2-70b")
GPUBaseConfig = ParentConfig.GPUBaseConfig


class OfflineGPUBaseConfig(GPUBaseConfig):
    scenario = Scenario.Offline
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    tensor_parallelism = 2
    pipeline_parallelism = 1
    precision = "fp16"
    enable_sort = False
    kvcache_free_gpu_mem_frac = 0.90
    min_duration = 2400000


class GH200_144GB_aarch64x1(OfflineGPUBaseConfig):
    gpu_batch_size = {'llama2-70b': 806}
    use_fp8 = True
    offline_expected_qps = 13
    enable_sort = False
    tensor_parallelism = 1


class GH200_144GB_aarch64x1_HighAccuracy(GH200_144GB_aarch64x1):
    pass


class H100_SXM_80GB_TP2x1(OfflineGPUBaseConfig):
    gpu_batch_size = {'llama2-70b': 896}
    use_fp8 = True
    offline_expected_qps = 19
    enable_sort = False
    tensor_parallelism = 2
    vboost_slider = 1


class H100_SXM_80GB_TP2x2(H100_SXM_80GB_TP2x1):
    offline_expected_qps = 19 * 2


class H100_SXM_80GB_TP2x4(H100_SXM_80GB_TP2x2):
    offline_expected_qps = 19 * 4


class H100_SXM_80GB_TP2x4_MaxQ(H100_SXM_80GB_TP2x4):
    offline_expected_qps = 66
    power_limit = 450


class H100_SXM_80GB_TP2x1_HighAccuracy(H100_SXM_80GB_TP2x1):
    pass


class H100_SXM_80GB_TP2x4_HighAccuracy(H100_SXM_80GB_TP2x4):
    pass


class H100_SXM_80GB_TP2x4_HighAccuracy_MaxQ(H100_SXM_80GB_TP2x4_MaxQ):
    pass


class H100_NVL_94GB_TP2x1(OfflineGPUBaseConfig):
    gpu_batch_size = {'llama2-70b': 1300}
    use_fp8 = True
    offline_expected_qps = 13
    enable_sort = False
    tensor_parallelism = 2


class H100_NVL_94GB_TP2x2(H100_NVL_94GB_TP2x1):
    offline_expected_qps = 25


class H100_NVL_94GB_TP2x4(H100_NVL_94GB_TP2x2):
    offline_expected_qps = 50
    gpu_rank_map = "0,3&1,2&4,5&6,7"


class H100_NVL_94GB_TP2x4_MaxQ(H100_NVL_94GB_TP2x4):
    offline_expected_qps = 45
    power_limit = 350


class H100_NVL_94GB_TP2x1_HighAccuracy(H100_NVL_94GB_TP2x1):
    pass


class H100_NVL_94GB_TP2x4_HighAccuracy(H100_NVL_94GB_TP2x4):
    pass


class H100_NVL_94GB_TP2x4_HighAccuracy_MaxQ(H100_NVL_94GB_TP2x4_MaxQ):
    pass


class H200_SXM_141GBx1(OfflineGPUBaseConfig):
    gpu_batch_size = {'llama2-70b': 806}
    use_fp8 = True
    offline_expected_qps = 13.4
    enable_sort = False
    tensor_parallelism = 1
    vboost_slider = 1


class H200_SXM_141GBx1_MaxQ(H200_SXM_141GBx1):
    pass


class H200_SXM_141GBx1_HighAccuracy(H200_SXM_141GBx1):
    pass


class H200_SXM_141GBx1_HighAccuracy_MaxQ(H200_SXM_141GBx1_MaxQ):
    pass


class H200_SXM_141GBx1_Triton(H200_SXM_141GBx1):
    use_triton = True


class H200_SXM_141GBx1_HighAccuracy_Triton(H200_SXM_141GBx1_HighAccuracy):
    use_triton = True


class H200_SXM_141GBx8(H200_SXM_141GBx1):
    offline_expected_qps = 104


class H200_SXM_141GBx8_MaxQ(H200_SXM_141GBx1_MaxQ):
    offline_expected_qps = H200_SXM_141GBx1_MaxQ.offline_expected_qps * 8


class H200_SXM_141GBx8_Triton(H200_SXM_141GBx8):
    use_triton = True


class H200_SXM_141GBx8_HighAccuracy(H200_SXM_141GBx8):
    pass


class H200_SXM_141GBx8_HighAccuracy_Triton(H200_SXM_141GBx8):
    use_triton = True


class H200_SXM_141GBx8_HighAccuracy_MaxQ(H200_SXM_141GBx8_MaxQ):
    pass


class H200_SXM_141GB_TP2x1(OfflineGPUBaseConfig):
    gpu_batch_size = {'llama2-70b': 2048}
    use_fp8 = True
    offline_expected_qps = 24
    enable_sort = False
    tensor_parallelism = 2


class H200_SXM_141GB_TP2x1_HighAccuracy(H200_SXM_141GB_TP2x1):
    pass


class H200_SXM_141GB_CTSx1(OfflineGPUBaseConfig):
    gpu_batch_size = {'llama2-70b': 784}
    use_fp8 = True
    offline_expected_qps = 13.5
    enable_sort = False
    tensor_parallelism = 1
    vboost_slider = 1


class H200_SXM_141GB_CTSx1_HighAccuracy(H200_SXM_141GB_CTSx1):
    pass


class H200_SXM_141GB_CTSx8(H200_SXM_141GB_CTSx1):
    offline_expected_qps = 120


class H200_SXM_141GB_CTSx8_HighAccuracy(H200_SXM_141GB_CTSx8):
    pass
