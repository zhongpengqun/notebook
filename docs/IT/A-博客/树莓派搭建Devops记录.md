# 准备工作
```
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

<details>
<summary></summary>

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

</details>

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