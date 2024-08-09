# 我的环境
树莓派4b
```
$ free -h
              总计         已用        空闲      共享    缓冲/缓存    可用
内存：        3.7G        1.6G        144M         33M        1.9G        2.0G
交换：          0B          0B          0B

$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.6 LTS
Release:        18.04
Codename:       bionic

$ lscpu
架构：           aarch64
字节序：         Little Endian
CPU:             4
在线 CPU 列表：  0-3
每个核的线程数： 1
每个座的核数：   4
座：             1
厂商 ID：        ARM
型号：           3
型号名称：       Cortex-A72
步进：           r0p3
CPU 最大 MHz：   1500.0000
CPU 最小 MHz：   600.0000
BogoMIPS：       108.00
L1d 缓存：       32K
L1i 缓存：       48K
L2 缓存：        1024K
标记：           fp asimd evtstrm crc32 cpuid
```

# 组件的安装
- minikube
按照官网步骤走，参考 https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Farm64%2Fstable%2Fbinary+download
```
$ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-arm64

$ sudo install minikube-linux-arm64 /usr/local/bin/minikube && rm minikube-linux-arm64
$ minikube start
```

但是可能报以下错误 ↓


```shell
$ minikube start
😄  Ubuntu 18.04 (arm64) 上的 minikube v1.33.1
✨  自动选择 docker 驱动。其他选项：none, ssh
📌  使用具有 root 权限的 Docker 驱动程序
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.44 ...
💾  正在下载 Kubernetes v1.30.0 的预加载文件...
    > index.docker.io/kicbase/sta...:  0 B [_____________________] ?% ? p/s 30s
    > preloaded-images-k8s-v18-v1...:  319.81 MiB / 319.81 MiB  100.00% 2.97 Mi
    > index.docker.io/kicbase/sta...:  0 B [_____________________] ?% ? p/s 30s
E0729 03:52:14.842324   26588 cache.go:189] Error downloading kic artifacts:  failed to download kic base image or any fallback image
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🤦  StartHost failed, but will try again: creating host: create: creating: setting up container node: preparing volume for minikube container: docker run --rm --name minikube-preload-sidecar --label created_by.minikube.sigs.k8s.io=true --label name.minikube.sigs.k8s.io=minikube --entrypoint /usr/bin/test -v minikube:/var gcr.io/k8s-minikube/kicbase:v0.0.44@sha256:eb04641328b06c5c4a14f4348470e1046bbcf9c2cbc551486e343d3a49db557e -d /var/lib: exit status 125
stdout:

stderr:
Unable to find image 'gcr.io/k8s-minikube/kicbase:v0.0.44@sha256:eb04641328b06c5c4a14f4348470e1046bbcf9c2cbc551486e343d3a49db557e' locally
docker: Error response from daemon: Get "https://gcr.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers).
See 'docker run --help'.

🤷  docker "minikube" 缺失 container，将重新创建。
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
😿  启动 docker container 失败。运行 "minikube delete" 可能需要修复它： recreate: creating host: create: creating: setting up container node: preparing volume for minikube container: docker run --rm --name minikube-preload-sidecar --label created_by.minikube.sigs.k8s.io=true --label name.minikube.sigs.k8s.io=minikube --entrypoint /usr/bin/test -v minikube:/var gcr.io/k8s-minikube/kicbase:v0.0.44@sha256:eb04641328b06c5c4a14f4348470e1046bbcf9c2cbc551486e343d3a49db557e -d /var/lib: exit status 125
stdout:

stderr:
Unable to find image 'gcr.io/k8s-minikube/kicbase:v0.0.44@sha256:eb04641328b06c5c4a14f4348470e1046bbcf9c2cbc551486e343d3a49db557e' locally
docker: Error response from daemon: Get "https://gcr.io/v2/": context deadline exceeded (Client.Timeout exceeded while awaiting headers).
See 'docker run --help'.
 

❌  因 GUEST_PROVISION 错误而退出：error provisioning guest: Failed to start host: recreate: creating host: create: creating: setting up container node: preparing volume for minikube container: docker run --rm --name minikube-preload-sidecar --label created_by.minikube.sigs.k8s.io=true --label name.minikube.sigs.k8s.io=minikube --entrypoint /usr/bin/test -v minikube:/var gcr.io/k8s-minikube/kicbase:v0.0.44@sha256:eb04641328b06c5c4a14f4348470e1046bbcf9c2cbc551486e343d3a49db557e -d /var/lib: exit status 125
stdout:

stderr:
Unable to find image 'gcr.io/k8s-minikube/kicbase:v0.0.44@sha256:eb04641328b06c5c4a14f4348470e1046bbcf9c2cbc551486e343d3a49db557e' locally
docker: Error response from daemon: Get "https://gcr.io/v2/": context deadline exceeded (Client.Timeout exceeded while awaiting headers).
See 'docker run --help'.


╭─────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                 │
│    😿  如果上述建议无法帮助解决问题，请告知我们：                                               │
│    👉  https://github.com/kubernetes/minikube/issues/new/choose                                 │
│                                                                                                 │
│    请运行 minikube logs --file=logs.txt 命令，并将生成的 logs.txt 文件附加到 GitHub 问题中。    │
│                                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────╯

```


尝试以下命令 ↓

```shell
$ minikube start --nodes 4 --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 4 --kubernetes-version=v1.23.1
😄  Ubuntu 18.04 (arm64) 上的 minikube v1.33.1
❗  当提供 --force 参数时，minikube 将跳过各种验证，这可能会导致意外行为

🙈  因 K8S_DOWNGRADE_UNSUPPORTED 错误而退出：无法安全地将现有的 Kubernetes v1.30.0 集群降级为 v1.23.1
💡  建议：

    1) 使用以下命令使用 Kubernetes 1.23.1 重新创建集群：
    
    minikube delete
    minikube start --kubernetes-version=v1.23.1
    
    2) 使用以下命令创建第二个具有 Kubernetes 1.23.1 的集群：
    
    minikube start -p minikube2 --kubernetes-version=v1.23.1
    
    3) 使用以下命令使用现有的 Kubernetes 1.30.0 版本的集群：
    
    minikube start --kubernetes-version=v1.30.0
```
按照提示
```shell
$ minikube delete
🔥  正在删除 docker 中的“minikube”…
🔥  正在移除 /home/ubuntu/.minikube/machines/minikube…
💀  已删除所有关于 "minikube" 集群的痕迹。
ubuntu@ubuntu:/home$ minikube start --kubernetes-version=v1.23.1
😄  Ubuntu 18.04 (arm64) 上的 minikube v1.33.1
✨  自动选择 docker 驱动。其他选项：none, ssh
📌  使用具有 root 权限的 Docker 驱动程序
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.44 ...
💾  正在下载 Kubernetes v1.23.1 的预加载文件...
    > index.docker.io/kicbase/sta...:  0 B [____________________] ?% ? p/s 1m0s
    > preloaded-images-k8s-v18-v1...:  27.08 MiB / 315.99 MiB  8.57% 138.65 KiB
    > index.docker.io/kicbase/sta...:  0 B [_____________________] ?% ? p/s 30s
E0729 05:56:55.791681   19614 cache.go:189] Error downloading kic artifacts:  failed to download kic base image or any fallback image
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🤦  StartHost failed, but will try again: creating host: create: creating: setting up container node: preparing volume for minikube container: docker run --rm --name minikube-preload-sidecar --label created_by.minikube.sigs.k8s.io=true --label name.minikube.sigs.k8s.io=minikube --entrypoint /usr/bin/test -v minikube:/var gcr.io/k8s-minikube/kicbase:v0.0.44@sha256:eb04641328b06c5c4a14f4348470e1046bbcf9c2cbc551486e343d3a49db557e -d /var/lib: exit status 125
stdout:

stderr:
Unable to find image 'gcr.io/k8s-minikube/kicbase:v0.0.44@sha256:eb04641328b06c5c4a14f4348470e1046bbcf9c2cbc551486e343d3a49db557e' locally
docker: Error response from daemon: Get "https://gcr.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers).
See 'docker run --help'.

🤷  docker "minikube" 缺失 container，将重新创建。
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
❗  The image 'registry.k8s.io/pause:3.6' was not found; unable to add it to cache.
❗  The image 'registry.k8s.io/kube-proxy:v1.23.1' was not found; unable to add it to cache.
❗  The image 'registry.k8s.io/kube-apiserver:v1.23.1' was not found; unable to add it to cache.
😿  启动 docker container 失败。运行 "minikube delete" 可能需要修复它： recreate: creating host: create: creating: setting up container node: preparing volume for minikube container: docker run --rm --name minikube-preload-sidecar --label created_by.minikube.sigs.k8s.io=true --label name.minikube.sigs.k8s.io=minikube --entrypoint /usr/bin/test -v minikube:/var gcr.io/k8s-minikube/kicbase:v0.0.44@sha256:eb04641328b06c5c4a14f4348470e1046bbcf9c2cbc551486e343d3a49db557e -d /var/lib: exit status 125
stdout:

stderr:
Unable to find image 'gcr.io/k8s-minikube/kicbase:v0.0.44@sha256:eb04641328b06c5c4a14f4348470e1046bbcf9c2cbc551486e343d3a49db557e' locally
docker: Error response from daemon: Get "https://gcr.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers).
See 'docker run --help'.
 

❌  因 GUEST_PROVISION 错误而退出：error provisioning guest: Failed to start host: recreate: creating host: create: creating: setting up container node: preparing volume for minikube container: docker run --rm --name minikube-preload-sidecar --label created_by.minikube.sigs.k8s.io=true --label name.minikube.sigs.k8s.io=minikube --entrypoint /usr/bin/test -v minikube:/var gcr.io/k8s-minikube/kicbase:v0.0.44@sha256:eb04641328b06c5c4a14f4348470e1046bbcf9c2cbc551486e343d3a49db557e -d /var/lib: exit status 125
stdout:

stderr:
Unable to find image 'gcr.io/k8s-minikube/kicbase:v0.0.44@sha256:eb04641328b06c5c4a14f4348470e1046bbcf9c2cbc551486e343d3a49db557e' locally
docker: Error response from daemon: Get "https://gcr.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers).
See 'docker run --help'.


╭─────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                 │
│    😿  如果上述建议无法帮助解决问题，请告知我们：                                               │
│    👉  https://github.com/kubernetes/minikube/issues/new/choose                                 │
│                                                                                                 │
│    请运行 minikube logs --file=logs.txt 命令，并将生成的 logs.txt 文件附加到 GitHub 问题中。    │
│                                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────╯

```

尝试失败了
```shell
$ minikube start --vm-driver=docker --base-image="docker.fxxk.dedyn.io/kicbase/stable:v0.0.32" --image-mirror-country='cn' --image-repository='registry.cn-hangzhou.aliyuncs.com/google_containers' --kubernetes-version=v1.23.8
😄  Ubuntu 18.04 (arm64) 上的 minikube v1.33.1
🆕  Kubernetes 1.30.0 现在可用。如果您想要升级，请指定：--kubernetes-version=v1.30.0
✨  根据现有的配置文件使用 docker 驱动程序
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.44 ...
🔄  Restarting existing docker container for "minikube" ...
🐳  正在 Docker 20.10.17 中准备 Kubernetes v1.23.8…
❌  无法加载缓存的镜像：loading cached images: stat /home/ubuntu/.minikube/cache/images/arm64/registry.k8s.io/kube-proxy_v1.23.8: no such file or directory
🔎  正在验证 Kubernetes 组件...
    ▪ 正在使用镜像 gcr.io/k8s-minikube/storage-provisioner:v5
❌  在 kubelet 中 检测到问题：
    Aug 07 02:12:30 minikube kubelet[6011]: E0807 02:12:30.052218    6011 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:12:32 minikube kubelet[6206]: E0807 02:12:32.007917    6206 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:12:34 minikube kubelet[6395]: E0807 02:12:34.015478    6395 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:12:36 minikube kubelet[6585]: E0807 02:12:36.203767    6585 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:12:38 minikube kubelet[6778]: E0807 02:12:38.014388    6778 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
❌  在 kubelet 中 检测到问题：
    Aug 07 02:12:46 minikube kubelet[7591]: E0807 02:12:46.491199    7591 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:12:48 minikube kubelet[7769]: E0807 02:12:48.576833    7769 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:12:50 minikube kubelet[7947]: E0807 02:12:50.487841    7947 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:12:52 minikube kubelet[8128]: E0807 02:12:52.494432    8128 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:12:54 minikube kubelet[8370]: E0807 02:12:54.500067    8370 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
❌  在 kubelet 中 检测到问题：
    Aug 07 02:12:56 minikube kubelet[8570]: E0807 02:12:56.685056    8570 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:12:58 minikube kubelet[8750]: E0807 02:12:58.465114    8750 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:00 minikube kubelet[8931]: E0807 02:13:00.227257    8931 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:02 minikube kubelet[9108]: E0807 02:13:02.004793    9108 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:03 minikube kubelet[9291]: E0807 02:13:03.973896    9291 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
❗  启用 'default-storageclass' 返回了错误: running callbacks: [sudo KUBECONFIG=/var/lib/minikube/kubeconfig /var/lib/minikube/binaries/v1.23.8/kubectl apply --force -f /etc/kubernetes/addons/storageclass.yaml: Process exited with status 1
stdout:

stderr:
The connection to the server localhost:8443 was refused - did you specify the right host or port?
]
❌  在 kubelet 中 检测到问题：
    Aug 07 02:13:10 minikube kubelet[9918]: E0807 02:13:10.231732    9918 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:12 minikube kubelet[10097]: E0807 02:13:12.026965   10097 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:14 minikube kubelet[10276]: E0807 02:13:14.024954   10276 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:16 minikube kubelet[10456]: E0807 02:13:16.118226   10456 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:18 minikube kubelet[10643]: E0807 02:13:18.201412   10643 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
❌  在 kubelet 中 检测到问题：
    Aug 07 02:13:23 minikube kubelet[11265]: E0807 02:13:23.986707   11265 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:25 minikube kubelet[11444]: E0807 02:13:25.763467   11444 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:27 minikube kubelet[11624]: E0807 02:13:27.786446   11624 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:29 minikube kubelet[11804]: E0807 02:13:29.738707   11804 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:31 minikube kubelet[11983]: E0807 02:13:31.979294   11983 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
❗  启用 'storage-provisioner' 返回了错误: running callbacks: [sudo KUBECONFIG=/var/lib/minikube/kubeconfig /var/lib/minikube/binaries/v1.23.8/kubectl apply --force -f /etc/kubernetes/addons/storage-provisioner.yaml: Process exited with status 1
stdout:

stderr:
The connection to the server localhost:8443 was refused - did you specify the right host or port?
]
🌟  启用插件： 
❌  在 kubelet 中 检测到问题：
    Aug 07 02:13:36 minikube kubelet[12424]: E0807 02:13:36.002379   12424 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:37 minikube kubelet[12604]: E0807 02:13:37.985770   12604 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:39 minikube kubelet[12782]: E0807 02:13:39.971831   12782 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:41 minikube kubelet[12973]: E0807 02:13:41.988488   12973 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:43 minikube kubelet[13150]: E0807 02:13:43.976034   13150 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
❌  在 kubelet 中 检测到问题：
    Aug 07 02:13:50 minikube kubelet[13779]: E0807 02:13:50.091474   13779 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:51 minikube kubelet[13958]: E0807 02:13:51.977115   13958 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:53 minikube kubelet[14138]: E0807 02:13:53.704636   14138 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:55 minikube kubelet[14316]: E0807 02:13:55.470208   14316 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:13:57 minikube kubelet[14499]: E0807 02:13:57.250393   14499 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
❌  在 kubelet 中 检测到问题：
    Aug 07 02:14:03 minikube kubelet[15117]: E0807 02:14:03.489760   15117 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:14:05 minikube kubelet[15296]: E0807 02:14:05.481647   15296 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:14:07 minikube kubelet[15472]: E0807 02:14:07.484189   15472 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:14:09 minikube kubelet[15648]: E0807 02:14:09.248409   15648 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
    Aug 07 02:14:11 minikube kubelet[15888]: E0807 02:14:11.289108   15888 kubelet.go:1431] "Failed to start ContainerManager" err="system validation failed - Following Cgroup subsystem not mounted: [memory]"
```

加上 minikube delete --all --purge 再运行一下, 貌似是minikube可以用了（`minikube -v`有输出），虽然报了错
```
$ minikube delete --all --purge
$ minikube start --vm-driver=docker --base-image="docker.fxxk.dedyn.io/kicbase/stable:v0.0.32" --image-mirror-country='cn' --image-repository='registry.cn-hangzhou.aliyuncs.com/google_containers' --kubernetes-version=v1.23.8
😄  Ubuntu 18.04 (arm64) 上的 minikube v1.33.1
✨  根据用户配置使用 docker 驱动程序
✅  正在使用镜像存储库 registry.cn-hangzhou.aliyuncs.com/google_containers
📌  使用具有 root 权限的 Docker 驱动程序
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.44 ...
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
    > kubelet.sha256:  64 B / 64 B [-------------------------] 100.00% ? p/s 0s
    > kubeadm.sha256:  64 B / 64 B [-------------------------] 100.00% ? p/s 0s
    > kubectl.sha256:  64 B / 64 B [-------------------------] 100.00% ? p/s 0s
    > kubeadm:  42.75 MiB / 42.75 MiB [----------] 100.00% 198.28 KiB p/s 3m41s
    > kubectl:  44.06 MiB / 44.06 MiB [----------] 100.00% 179.53 KiB p/s 4m12s
    > kubelet:  116.72 MiB / 116.72 MiB [--------] 100.00% 373.34 KiB p/s 5m20s

    ▪ 正在生成证书和密钥...
    ▪ 正在启动控制平面...
💢  初始化失败，将再次重试：wait: /bin/bash -c "sudo env PATH="/var/lib/minikube/binaries/v1.23.8:$PATH" kubeadm init --config /var/tmp/minikube/kubeadm.yaml  --ignore-preflight-errors=DirAvailable--etc-kubernetes-manifests,DirAvailable--var-lib-minikube,DirAvailable--var-lib-minikube-etcd,FileAvailable--etc-kubernetes-manifests-kube-scheduler.yaml,FileAvailable--etc-kubernetes-manifests-kube-apiserver.yaml,FileAvailable--etc-kubernetes-manifests-kube-controller-manager.yaml,FileAvailable--etc-kubernetes-manifests-etcd.yaml,Port-10250,Swap,NumCPU,Mem,SystemVerification,FileContent--proc-sys-net-bridge-bridge-nf-call-iptables": Process exited with status 1
stdout:
[init] Using Kubernetes version: v1.23.8
[preflight] Running pre-flight checks
[preflight] The system verification failed. Printing the output from the verification:
KERNEL_VERSION: 5.4.0-1028-raspi
CONFIG_NAMESPACES: enabled
CONFIG_NET_NS: enabled
CONFIG_PID_NS: enabled
CONFIG_IPC_NS: enabled
CONFIG_UTS_NS: enabled
CONFIG_CGROUPS: enabled
CONFIG_CGROUP_CPUACCT: enabled
CONFIG_CGROUP_DEVICE: enabled
CONFIG_CGROUP_FREEZER: enabled
CONFIG_CGROUP_PIDS: enabled
CONFIG_CGROUP_SCHED: enabled
CONFIG_CPUSETS: enabled
CONFIG_MEMCG: enabled
CONFIG_INET: enabled
CONFIG_EXT4_FS: enabled
CONFIG_PROC_FS: enabled
CONFIG_NETFILTER_XT_TARGET_REDIRECT: enabled (as module)
CONFIG_NETFILTER_XT_MATCH_COMMENT: enabled (as module)
CONFIG_FAIR_GROUP_SCHED: enabled
CONFIG_OVERLAY_FS: enabled (as module)
CONFIG_AUFS_FS: enabled (as module)
CONFIG_BLK_DEV_DM: enabled
CONFIG_CFS_BANDWIDTH: enabled
CONFIG_CGROUP_HUGETLB: not set - Required for hugetlb cgroup.
CONFIG_SECCOMP: enabled
CONFIG_SECCOMP_FILTER: enabled
DOCKER_VERSION: 20.10.17
DOCKER_GRAPH_DRIVER: overlay2
OS: Linux
CGROUPS_CPU: enabled
CGROUPS_CPUACCT: enabled
CGROUPS_CPUSET: enabled
CGROUPS_DEVICES: enabled
CGROUPS_FREEZER: enabled
CGROUPS_MEMORY: missing
CGROUPS_PIDS: enabled
CGROUPS_HUGETLB: missing
[preflight] Pulling images required for setting up a Kubernetes cluster
[preflight] This might take a minute or two, depending on the speed of your internet connection
[preflight] You can also perform this action in beforehand using 'kubeadm config images pull'
[certs] Using certificateDir folder "/var/lib/minikube/certs"
[certs] Using existing ca certificate authority
[certs] Using existing apiserver certificate and key on disk
[certs] Generating "apiserver-kubelet-client" certificate and key
[certs] Generating "front-proxy-ca" certificate and key
[certs] Generating "front-proxy-client" certificate and key
[certs] Generating "etcd/ca" certificate and key
[certs] Generating "etcd/server" certificate and key
[certs] etcd/server serving cert is signed for DNS names [localhost minikube] and IPs [192.168.49.2 127.0.0.1 ::1]
[certs] Generating "etcd/peer" certificate and key
[certs] etcd/peer serving cert is signed for DNS names [localhost minikube] and IPs [192.168.49.2 127.0.0.1 ::1]
[certs] Generating "etcd/healthcheck-client" certificate and key
[certs] Generating "apiserver-etcd-client" certificate and key
[certs] Generating "sa" key and public key
[kubeconfig] Using kubeconfig folder "/etc/kubernetes"
[kubeconfig] Writing "admin.conf" kubeconfig file
[kubeconfig] Writing "kubelet.conf" kubeconfig file
[kubeconfig] Writing "controller-manager.conf" kubeconfig file
[kubeconfig] Writing "scheduler.conf" kubeconfig file
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Starting the kubelet
[control-plane] Using manifest folder "/etc/kubernetes/manifests"
[control-plane] Creating static Pod manifest for "kube-apiserver"
[control-plane] Creating static Pod manifest for "kube-controller-manager"
[control-plane] Creating static Pod manifest for "kube-scheduler"
[etcd] Creating static Pod manifest for local etcd in "/etc/kubernetes/manifests"
[wait-control-plane] Waiting for the kubelet to boot up the control plane as static Pods from directory "/etc/kubernetes/manifests". This can take up to 4m0s
[kubelet-check] Initial timeout of 40s passed.

        Unfortunately, an error has occurred:
                timed out waiting for the condition

        This error is likely caused by:
                - The kubelet is not running
                - The kubelet is unhealthy due to a misconfiguration of the node in some way (required cgroups disabled)

        If you are on a systemd-powered system, you can try to troubleshoot the error with the following commands:
                - 'systemctl status kubelet'
                - 'journalctl -xeu kubelet'

        Additionally, a control plane component may have crashed or exited when started by the container runtime.
        To troubleshoot, list all containers using your preferred container runtimes CLI.

        Here is one example how you may list all Kubernetes containers running in docker:
                - 'docker ps -a | grep kube | grep -v pause'
                Once you have found the failing container, you can inspect its logs with:
                - 'docker logs CONTAINERID'


stderr:
        [WARNING SystemVerification]: missing optional cgroups: hugetlb
        [WARNING SystemVerification]: missing required cgroups: memory
        [WARNING Service-Kubelet]: kubelet service is not enabled, please run 'systemctl enable kubelet.service'
error execution phase wait-control-plane: couldn't initialize a Kubernetes cluster
To see the stack trace of this error execute with --v=5 or higher
```
随后试试kubectl
```
$ kubectl get ns
E0807 02:49:53.261494  191354 memcache.go:265] couldn't get current server API group list: Get "http://localhost:8080/api?timeout=32s": dial tcp 127.0.0.1:8080: connect: connection refused
E0807 02:49:53.262802  191354 memcache.go:265] couldn't get current server API group list: Get "http://localhost:8080/api?timeout=32s": dial tcp 127.0.0.1:8080: connect: connection refused
E0807 02:49:53.263705  191354 memcache.go:265] couldn't get current server API group list: Get "http://localhost:8080/api?timeout=32s": dial tcp 127.0.0.1:8080: connect: connection refused
E0807 02:49:53.264814  191354 memcache.go:265] couldn't get current server API group list: Get "http://localhost:8080/api?timeout=32s": dial tcp 127.0.0.1:8080: connect: connection refused
E0807 02:49:53.265598  191354 memcache.go:265] couldn't get current server API group list: Get "http://localhost:8080/api?timeout=32s": dial tcp 127.0.0.1:8080: connect: connection refused
The connection to the server localhost:8080 was refused - did you specify the right host or port?
```
