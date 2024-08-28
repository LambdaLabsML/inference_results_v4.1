#! /bin/bash 
# Copyright (c) 2024, NVIDIA CORPORATION. All rights reserved.
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

case $OMPI_COMM_WORLD_LOCAL_RANK in
[0]) 
    cpu=0
    mem=0
    ;;
[1])
    cpu=0
    mem=0
    ;;
[2])
    cpu=0
    mem=0
    ;;
[3])
    cpu=0
    mem=0
    ;;
[4]) 
    cpu=1
    mem=1
    ;;
[5])
    cpu=1
    mem=1
    ;;
[6])
    cpu=1
    mem=1
    ;;
[7])
    cpu=1
    mem=1
    ;;
[8])
    cpu=0
    mem=0
    ;;
[9])
    cpu=0
    mem=0
    ;;
[10])
    cpu=0
    mem=0
    ;;
[11])
    cpu=0
    mem=0
    ;;
[12])
    cpu=1
    mem=1
    ;;
[13])
    cpu=1
    mem=1
    ;;
[14])
    cpu=1
    mem=1
    ;;
[15])
    cpu=1
    mem=1
    ;;
[16])
    cpu=0
    mem=0
    ;;
[17])
    cpu=0
    mem=0
    ;;
[18])
    cpu=0
    mem=0
    ;;
[19])
    cpu=0
    mem=0
    ;;
[20])
    cpu=1
    mem=1
    ;;
[21])
    cpu=1
    mem=1
    ;;
[22])
    cpu=1
    mem=1
    ;;
[23])
    cpu=1
    mem=1
    ;;
[24])
    cpu=0
    mem=0
    ;;
[25])
    cpu=0
    mem=0
    ;;
[26])
    cpu=0
    mem=0
    ;;
[27])
    cpu=0
    mem=0
    ;;
[28])
    cpu=1
    mem=1
    ;;
[29])
    cpu=1
    mem=1
    ;;
[30])
    cpu=1
    mem=1
    ;;
[31])
    cpu=1
    mem=1
    ;;
[32])
    cpu=0
    mem=0
    ;;
esac
numactl --cpunodebind=$cpu --membind=$mem $@
