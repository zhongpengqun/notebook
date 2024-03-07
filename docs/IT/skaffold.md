- Skaffold
  - https://skaffold.dev
  - [django-postgres-skaffold-k8s]: https://github.com/ksaaskil/django-postgres-skaffold-k8s
  - Installation
      - Is there vscode skaffold plugin ?
          - No, 2023年1月29日18:33:23
      - https://skaffold.dev/docs/install/

```shell
curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-amd64 && sudo install skaffold /usr/local/bin/

$ skaffold init
WARN[0000] Skipping Jib: no JVM: [java -version] failed: exec: "java": executable file not found in $PATH  subtask=-1 task=DevLoop
one or more valid Kubernetes manifests are required to run skaffold

[resolve] https://www.zhangbj.com/p/1223.html
skaffold init --generate-manifests
```

        - https://cloud.tencent.com/developer/news/486219

        ```
        -----
        Skaffold能够实时监控源码文件的变化，当发生变化后即可触发Skaffold配置的流水线，进行构建部署。因此，Skaffold的适用阶段为Kubernetes应用程序的本地开发调试。主要是满足本地开发阶段代码质量的检查，将问题发现和修复前移到开发阶段，这也是DevOps中的最佳实践。

        ----
        Skaffold只需要提供一个客户端，该客户端可以本地安装也可以使用Docker容器    // todo 测试下docker的安装

        ----
        如何在skaffold.yaml中配置比如pylint检测 ？

        ----
        也就是说，开发人员只需要对代码进行修改，剩下的工作全部交给Skaffold，就可以测试变更后的代码了。

        ----
        代码变更后，首先就要执行构建阶段，Skaffold原生支持几种不同的构建镜像的工具。比如Dockerfile、Jib Maven and Gradle、Bazel、Cloud Native Buildpacks以及Custom Script

        so, 不应该只有docker的吗 ？

        ----
        skaffold init 指定作用的文件夹，因为我发现执行init的时候，外围的文件夹的dockerfile文件也会被detect到

        ----
        skaffold如何和helm，kustomize合用 ？

        ```

    - skaffold run
    ```shell
    # skaffold run
    WARN[0005] failed to detect active kubernetes cluster node platform. Specify the correct build platform in the `skaffold.yaml` file or using the `--platform` flag  subtask=-1 task=DevLoop
    Generating tags...
     - skaffold-example -> skaffold-example:latest
    Some taggers failed. Rerun with -vdebug for errors.
    Checking cache...
     - skaffold-example: Not found. Building
    Starting build...
    Building [skaffold-example]...
    Sending build context to Docker daemon  4.096kB
    Step 1/10 : FROM golang:1.18 as builder
    build [skaffold-example] failed: docker build failure: Error parsing reference: "golang:1.18 as builder" is not a valid repository/tag: invalid reference format. Please fix the Dockerfile and try again..

    [solution]
    root cause: docker version is lower than 17.05+
    \# docker -v
    Docker version 1.13.1, build 0be3e21/1.13.1
    ```

    ```shell
    # skaffold run
    WARN[0001] failed to detect active kubernetes cluster node platform. Specify the correct build platform in the `skaffold.yaml` file or using the `--platform` flag  subtask=-1 task=DevLoop
    Generating tags...
    - dockerfile-image -> dockerfile-image:latest
    Some taggers failed. Rerun with -vdebug for errors.
    Checking cache...
    - dockerfile-image: Not found. Building
    Starting build...
    Building [dockerfile-image]...
    Sending build context to Docker daemon  3.072kB
    Step 1/3 : FROM python:3.6
    ---> 54260638d07c
    Step 2/3 : COPY test.py test.py
    ---> a0b20922d9aa
    Step 3/3 : CMD python3 test.py
    ---> Running in d5f757102891
    ---> 769393e0793c
    Successfully built 769393e0793c

    build [dockerfile-image] failed: could not push image "dockerfile-image:latest": Error response from daemon: You cannot push a "root" repository. Please rename your repository to docker.io/<user>/<repo> (ex: docker.io/<user>/dockerfile-image)

    [ solution ]
    // todo
    ```

    - skaffold.yaml
    ```yaml
    xx
    ```
    - skaffold render

    ```shell
    \# skaffold build
    Generating tags...
     - django-store -> django-store:64a8d65
     - django-store-nginx -> django-store-nginx:64a8d65
    Checking cache...
     - django-store: Not found. Building
     - django-store-nginx: Not found. Building
    Starting build...
    Building [django-store-nginx]...
    Sending build context to Docker daemon  3.584kB
    Step 1/2 : FROM nginx:1.16.1
    Trying to pull repository docker.io/library/nginx ... 
    Building [django-store]...
    Build [django-store] was canceled
    docker build failure: Get https://registry-1.docker.io/v2/: net/http: request canceled (Client.Timeout exceeded while awaiting headers). Please fix the Dockerfile and try again..

    Solution: https://blog.csdn.net/zzddada/article/details/117750784
    But

    \# skaffold build
    Generating tags...
     - django-store -> django-store:64a8d65
     - django-store-nginx -> django-store-nginx:64a8d65
    Checking cache...
     - django-store: Not found. Building
     - django-store-nginx: Not found. Building
    Starting build...
    Building [django-store-nginx]...
    Sending build context to Docker daemon  3.584kB
    Step 1/2 : FROM nginx:1.16.1
    Trying to pull repository docker.io/library/nginx ... 
    1.16.1: Pulling from docker.io/library/nginx
    54fec2fa59d0: Pulling fs layer
    5546cfc92772: Pulling fs layer
    50f62e3cdaf7: Pulling fs layer
    50f62e3cdaf7: Verifying Checksum
    50f62e3cdaf7: Download complete
    54fec2fa59d0: Verifying Checksum
    54fec2fa59d0: Download complete
    5546cfc92772: Verifying Checksum
    5546cfc92772: Download complete
    54fec2fa59d0: Pull complete
    5546cfc92772: Pull complete
    50f62e3cdaf7: Pull complete
    Digest: sha256:d20aa6d1cae56fd17cd458f4807e0de462caf2336f0b70b5eeb69fcaaf30dd9c
    Status: Downloaded newer image for docker.io/nginx:1.16.1
     ---> dfcfd8e9a5d3
    Step 2/2 : COPY nginx.conf /etc/nginx/nginx.conf
     ---> ab0bef3cb59e
    Successfully built ab0bef3cb59e
    Building [django-store]...
    Build [django-store] was canceled
    could not push image "django-store-nginx:64a8d65": Error response from daemon: You cannot push a "root" repository. Please rename your repository to docker.io/<user>/<repo> (ex: docker.io/<user>/django-store-nginx)

    // Modify image name as `docker.io/zhongpengqun/django-store-nginx` in yaml file
    ...
     - Use "kubectl options" for a list of global command-line options (applies to all commands).
     - 
     - Error: unknown flag: --wait
    Cleaning up resources encountered an error, will continue to clean up other resources.
    Build Failed. No push access to specified image repository. Try running with `--default-repo` flag. Otherwise start a local kubernetes cluster like `minikube`.
    ```

- skaffold config set --global default-repo localhost:5000
