# 环境
```
版本	Windows 10 专业版
版本号	22H2
安装日期	‎2023/‎12/‎19
操作系统内部版本	19045.4651
体验	Windows Feature Experience Pack 1000.19060.1000.0
```
```
设备名称	ZL-20231219TEWC
处理器	12th Gen Intel(R) Core(TM) i7-12700   2.10 GHz
机带 RAM	16.0 GB (15.7 GB 可用)
设备 ID	DAD38684-CCF4-42C7-AC51-9C39AC2C1C3E
产品 ID	00331-10000-00001-AA346
系统类型	64 位操作系统, 基于 x64 的处理器
笔和触控	没有可用于此显示器的笔或触控输入
```
```
C:\Users\zlzk>nvidia-smi
Wed Aug 14 10:44:50 2024
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 536.23                 Driver Version: 536.23       CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                     TCC/WDDM  | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3050      WDDM  | 00000000:01:00.0  On |                  N/A |
|  0%   45C    P8              46W / 115W |    166MiB /  8192MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+

+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
+---------------------------------------------------------------------------------------+
```

从官网下载对应的CUDA版本,我安装12.0
- https://developer.nvidia.com/cuda-12-0-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local




# CPU版本
```
conda install pytorch torchvision torchaudio cpuonly -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/win-64/
```

# References
- https://blog.csdn.net/merisc/article/details/139856501