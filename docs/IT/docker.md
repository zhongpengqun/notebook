### Docker
- Docker
    - Use case of docker tags
    - Is it possible that 2 same pods run on one k8s node ?
    - What is overlay ?
    - Network
      - Bridge
      - Host
      - ...
    - docker manifest
    - `Docker Orchestration Files`
    - docker sbom command
    - Configmap
    - 进入pod与进入container的区别？
    - How to get docker disk usage ?  `docker system df`
    - docker stop then remove all containers
        - `docker stop $(docker ps -aq)`
    - run container from dockerfile
    ```shell
    docker build -t xxx .  
    docker run -d xxx

    # ↓ docker build from file
    docker build - < Dockerfile
    ```
        - Build with -
            - https://docs.docker.com/engine/reference/commandline/build/#build-with--

    - `docker ps` vs `docker ps -a`

    - docker --detach
    - delete a container file from outside of container.
    - docker exec -it -u 0 osstpmgt_websvc_1 bash  以root用户进入container
    - docker如何实现重新打tag并删除原tag的镜像?  https://blog.csdn.net/Dontla/article/details/122868804
    - 如果pg_restore一个db.dump到docker container中，如果这个container stop了，这个数据库的内容是否也消失了?
    - `Sending build context to Docker daemon  26.44GB`
        - 考虑当前目录下是否有大文件
        - 
    - 实现docker run mycmd, 然后mycmd可以在host上执行，这样的dockerfile怎么写？
    - /var/lib/docker/containers
    - container的log保存在container内部的什么位置?是否保存在container的内部？

    - 在阿里云中看到有`容器运行时`--containerd 1.5.13 与 安全沙箱2.2.2的字样，什么意思？
        - https://cs.console.aliyun.com/?spm=a2c6h.12873639.article-detail.4.6ade4960sj8Igz#/k8s/cluster/createV2/managed?template=pro-standard

#### Dockerfile
    - USER
    - ARG
    - COPY --chown
    - RUN & CMD & ENTRYPOINT
        - RUN executes commands and creates new image layers
            - RUN 经常用于安装软件包
        - CMD命令是当Docker镜像被启动后Docker容器将会默认执行的命令。
            - However CMD can be replaced by docker run command line parameters.
            - Dockerfile中只有一条CMD指定，如果列出多个，只有最后一个CMD才会生效
        - ENTRYPOINT configures the command to run when the container starts, similar to CMD from a functionality perspective
            - 只有一条ENTRYPOINT指定，如果列出多个，只有最后一个生效
            - dockerfile中ENTRYPOINT ["ls"]， 如果docker run entrypoint-demo:latest -alh，则执行 ls -alh
                - 但是如果是 CMD ["ls"]， 则 docker run entrypoint-demo:latest -alh 会报错
                - 同时提供 ENTRYPOINT ["ls"]，CMD ["-alh"]，会执行 ls -alh, 但是此时我们run的时候可以用参数覆盖CMD的
    - `$PATH`
    - `ENV PYTHONIOENCODING UTF-8`

- Dockerfile 中的 FROM 能 FROM 本地的一个 image 吗？

```yaml
Here is an example from skaffold examples:
My questions:
- Why 2 `FROM` ?
- COPY --from
- Can you explain each line ?
references: https://blog.csdn.net/a772304419/article/details/126644409

---------------
FROM golang:1.18 as builder
WORKDIR /code
COPY main.go .
COPY go.mod .
# `skaffold debug` sets SKAFFOLD_GO_GCFLAGS to disable compiler optimizations
ARG SKAFFOLD_GO_GCFLAGS
RUN go build -gcflags="${SKAFFOLD_GO_GCFLAGS}" -trimpath -o /app main.go

FROM alpine:3
# Define GOTRACEBACK to mark this container as using the Go language runtime
# for `skaffold debug` (https://skaffold.dev/docs/workflows/debug/).
ENV GOTRACEBACK=single
CMD ["./app"]
COPY --from=builder /app .
```

```shell
$ systemctl restart docker
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===
Authentication is required to restart 'docker.service'.
Authenticating as: vz
Password: 
==== AUTHENTICATION COMPLETE ===
Job for docker.service failed because the control process exited with error code.
See "systemctl status docker.service" and "journalctl -xe" for details.
-----
solution:
https://ithelp.ithome.com.tw/m/articles/10294103
https://blog.51cto.com/u_15162069/2743910
```

- systemd

- Docker-compose
- kubectl
  - kubectl create & kubectl apply
  - Services
    - ClusterIp (Default)
    - NodePort
    - 
  - restart: unless-stopped
  - kubectl diff

- Dockerfile
  - VOLUME
    - When do we need VOLUME 
    - 3 docker volume types
  - COPY --from=builder /opt/static static

- Docker stop all containers
    - stop all containers: `docker stop $(docker ps -aq)`
    - remove all containers: `docker rm $(docker ps -aq)`
    - delete all images `docker rmi $(docker images -q)`
- Why during my usage of docker, the docker disk usage is bigger and bigger ?
- docker network
- docker-compose `ports`, left or right is container port ?
- Host-port:Container-port

- Which command both in docker and docker-compose, is there any difference in usage in docker and docker-compose ?
- docker save & docker export  /  docker import & docker load
    - docker export -o english-db-`date +%Y%m%d-%H:%M:%S`.tar c7962a4fee17
        - 使用 docker export 命令根据容器 ID 将镜像导出成一个文件。
            - docker export f299f501774c > hangger_server.tar
            - 使用 docker import 命令则可将这个镜像文件导入进来。
                - docker import - new_hangger_server < hangger_server.tar
    - save 和 load 这两个命令是通过镜像来保存、加载镜像文件的

- dockerfile中export失效，在dockerfile中的RUN中export，但是进入container后，echo该变量，并没有
    - 可以用ENV
    - 相关的问题
        - How to export an environment variable to a docker image?
            - https://stackoverflow.com/questions/41315737/how-to-export-an-environment-variable-to-a-docker-image


- save docker running container and push to dockerhub
```shell
docker commit 0a887a75b48b centos5.8-pkgs-and-tools-preinstalled:v1
docker tag centos5.8-pkgs-and-tools-preinstalled:v1 zhongpengqun/centos5.8-pkgs-and-tools-preinstalled:v1
docker push zhongpengqun/centos5.8-pkgs-and-tools-preinstalled:v1
```

### docker-compose
- Why `links` ? Is it has any association with `depends_on` ?

- `docker-compose build` 的作用是什么？
    - 由 dockerfile 构建一个docker image ？

`depends_on` determines the order of create containers.

An example
```yaml
version: '3.6'     # version of format of this yaml file, it can be 1, 2.x, 3.x, it's matter of the compatible with docker
services:
    nginx:
        build:
            context: fish        
            dockerfile: Dockerfile.nginx    # dockerfile is located at fish/Dockerfile.nginx
        restart: always     # it's equal to `docker run --restart always`, it is one kind of `restart policies`, 
                            # docker daemon will always try to restart the container infinitely until container starts successfully.
        links:          
            - gunicorn    # By links, gunicorn:80 will works, same as 10.0.0.4:80
        volumes:
            - nfs-storage:/build/toolchain    # `nfs-storage` is defined in below high level `volumes` block.
            - "./runtime/fish_nginx.conf:/etc/nginx/sites-available/fish.conf:ro"     # mount local file into container
        ports:
            - "80:80"   # host-port: container-port

    gunicorn:
        image: "fish_django_backend"    # my guess: 
        build:
            context: fish
            dockerfile: Dockerfile.django
        command: ["./bin/gunicorn_entrypoint.sh"]
        restart: always
        links:
            - db
            - couchdb
            - rabbitmq
        volumes:
            - nfs-storage:/build/toolchain
        expose:
            - "8000"
        ports:
            - "8001:8000"
        secrets:
            - host_ssh_key    # `host_ssh_key` is declared below, in high level block `secrets`

    coder_manager:
        image: "fish_django_backend"
        build:
            context: buildaudit
            dockerfile: Dockerfile.django
        command: ["./manage.py", "service_appcheck_manager"]
        restart: always
        links:
            - db
            - rabbitmq
        volumes:
            - "./runtime/buildaudit.yaml:/opt/buildaudit.yaml"

    coder:
        build:
            context: coder
            # here no `dockerfile` argument, so it will run the default `Dockerfile` file, i guess..
        links:
            - rabbitmq
        restart: always

    rabbitmq:
        build:
            context: ./rabbitmq
        expose:
            - "5672"
            - "15672"
        ports:
            - "15673:15672"
            - "5673:5672"
        environment:
            - RABBITMQ_DEFAULT_USER=admin
            - RABBITMQ_DEFAULT_PASS=123456

    db:
        image: postgres:11.9
        expose:
            - "5432"
        ports:
            - "5433:5432"
        environment:
            - POSTGRES_USER=root
            - POSTGRES_PASSWORD=123456
        command: "-c config_file=/etc/postgresql/postgresql.conf"
        volumes:
            - "./runtime/fish-postgres.conf:/etc/postgresql/postgresql.conf"

    couchdb:
        build:
            context: couchdb
            dockerfile: Dockerfile
        restart: always
        environment:
            - COUCHDB_USER=123456
            - COUCHDB_PASSWORD=123456
        expose:
            - "5984"
        ports:
            - "5984:5984"
        volumes:
            - "./db/couchdb_data:/opt/couchdb/data"

volumes:      # Declare all volumes in this list, it's convenient to be referred by many places
    nfs-storage:
        driver: local
        driver_opts:
            type: nfs
            o: "addr=storage.micro-hard.com,ro,nolock"
            device: ":/storage1"

secrets:
    host_ssh_key:
        file: ~/.ssh/id_rsa
```

- docker-compose run --rm --entrypoint 


# docker-compose up -d
[+] Running 0/0
 ⠿ Network concourse_default  Error                                                                                                                                        0.0s
failed to create network concourse_default: Error response from daemon: Failed to Setup IP tables: Unable to enable SKIP DNAT rule:  (iptables failed: iptables --wait -t nat -I DOCKER -i br-7b98d6e4dcfd -j RETURN: iptables: No chain/target/match by that name.
 (exit status 1))

[resolved]
# systemctl restart docker.service
# docker-compose up -d
```

```shell
docker-compose up --detach --build gunicorn
docker-compose up --build gunicorn
```

- How to Rebuild and restart container ?
- How do I run a docker instance from a DockerFile?


install docker on ubuntu
```shell
apt-get install docker.io
```

linux install docker-compose

```shell
https://github.com/docker/compose/releases/tag/v2.10.2
https://github.com/docker/compose/releases/download/v2.10.2/docker-compose-linux-x86_64
```

- export NETWORK_CONFIG="--net=host"


```shell
$ docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: zhongpengqun
Password: 
** Message: 16:34:45.997: Remote error from secret service: org.freedesktop.DBus.Error.ServiceUnknown: The name org.freedesktop.secrets was not provided by any .service files
Error saving credentials: error storing credentials - err: exit status 1, out: `The name org.freedesktop.secrets was not provided by any .service files`


s:
sudo apt install gnupg2 pass

```

- Is there any dockerhub alternative ?
    - AWS ECR Public ？
        - Push and pull from AWS ECR 
            - official tutorial: https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html
            - [prefer] https://www.youtube.com/watch?v=89ZeXaZEf80
            - https://www.youtube.com/watch?v=8XnqgiQaIkU
                - AmazonEC2ContainerRegistryFullAccess
                - 需要安装aws v2的client
                    - 如何安装？
                        https://devopsmania.com/how-to-install-aws-cli-v2-on-linux/
                        ```
                        curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
                        unzip awscliv2.zip
                        sudo ./aws/install
                        /usr/local/bin/aws --version
                        ```
                - errors encountered
                ```
                $ aws ecr-public get-login-password --region us-east-1

                An error occurred (UnrecognizedClientException) when calling the GetAuthorizationToken operation: The security token included in the request is invalid.

                s:
                $ aws configure
                $ AWS Access Key ID [****************E5TA]=xxxxxxxxxx
                $ AWS Secret Access Key [****************7gNT]=xxxxxxxxxxxxxx
                ↑ how to create access key ?
                open page https://us-east-1.console.aws.amazon.com/iamv2/home#/security_credentials
                Then succeed !
                $ aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/y5z1i2v3
                WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
                Configure a credential helper to remove this warning. See
                https://docs.docker.com/engine/reference/commandline/login/#credentials-store

                Login Succeeded
                    - May raise
                    ```
                    Error: Cannot perform an interactive login from a non TTY device
                    ```    
                    ```
                    $ /usr/local/bin/aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/y5z1i2v3
                    ** Message: 01:04:12.837: Remote error from secret service: org.freedesktop.DBus.Error.ServiceUnknown: The name org.freedesktop.secrets was not provided by any .service files
                    Error saving credentials: error storing credentials - err: exit status 1, out: `The name org.freedesktop.secrets was not provided by any .service files`

                    $ apt -y install gnome-keyring

                    $ /usr/local/bin/aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/y5z1i2v3
                    ** Message: 01:08:59.361: Remote error from secret service: org.freedesktop.DBus.Error.UnknownMethod: No such interface 'org.freedesktop.Secret.Collection' on object at path /org/freedesktop/secrets/collection/login
                    Error saving credentials: error storing credentials - err: exit status 1, out: `No such interface 'org.freedesktop.Secret.Collection' on object at path /org/freedesktop/secrets/collection/login`

                    Solution: https://juejin.cn/post/7226239012389584956
                    sudo apt install golang-docker-credential-helpers gnupg2 pass
                    ```

                Push images to AWS registry
                $ docker push public.ecr.aws/y5z1i2v3/vincent-jenkins:latest
                The push refers to repository [public.ecr.aws/y5z1i2v3/vincent-jenkins]
                a0db388da653: Preparing 
                5ace2236b792: Preparing 
                e8730b8130f7: Preparing 
                71172cb73530: Preparing 
                e8d54b9aa21c: Preparing 
                2bb413634e22: Waiting 
                1b0f52754622: Waiting 
                781a4a82dd8d: Waiting 
                2b19e8927d12: Waiting 
                e0d74c92d90b: Waiting 
                0fc1f85308ed: Waiting 
                0920ece9e11d: Waiting 
                5cb40c97b600: Waiting 
                9ece0f31ab3f: Waiting 
                dced136831e2: Waiting 
                50c172b1f6cb: Waiting 
                fc340cdaad0c: Waiting 
                172cb7ad177f: Waiting 
                4fa6c90606ff: Waiting 
                912e23b84980: Waiting 
                de5af37ebe4a: Waiting 
                7f03bfe4d6dc: Waiting 
                name unknown: The repository with name 'vincent-jenkins' does not exist in the registry with id 'y5z1i2v3'

                s:
                docker push public.ecr.aws/y5z1i2v3/zhongpengqun:latest
                ```
                - vincent's repos page
                    - https://us-east-1.console.aws.amazon.com/ecr/repositories?region=us-east-1

                - 吐槽/疑惑：aws的repo概念上只对应一个image ？

- docker pull from private registry ?
    - how to deploy a private registry ?
        - https://www.youtube.com/watch?v=O_NMIZJ1qvw
        ```
        docker run -d -p 15000:5000 --restart=always --name registry -v $(pwd)/docker-registry:/var/lib/registry registry:latest

        // docker安装后默认没有daemon.json这个配置文件，需要进行手动创建.
        $ cat /etc/docker/daemon.json
        {
            "insecure-registries":[
                "139.196.39.92:15000"
            ]
        }

        curl -X GET http://139.196.39.92:15000/v2/_catalog
        If you encounter below error
        curl: (56) Recv failure: Connection reset by peer
        


        docker tag nginx 139.196.39.92:15000/nginx

        $ docker push 139.196.39.92:15000/nginx
        Using default tag: latest
        The push refers to repository [139.196.39.92:15000/nginx]
        ff4557f62768: Pushed 
        4d0bf5b5e17b: Pushed 
        95457f8a16fd: Pushed 
        a0b795906dc1: Pushed 
        af29ec691175: Pushed 
        3af14c9a24c9: Pushed 
        latest: digest: sha256:bfb112db4075460ec042ce13e0b9c3ebd982f93ae0be155496d050bb70006750 size: 1570


        Pull image from this private registry.

        ```
            - Is there an UI for it ?
                - No, it's just a backend service, no ui
        - https://www.baeldung.com/ops/docker-private-registry
            - How to backup and migrate ?


- 宿主机是把自己的端口映射到container里作为container的ip的吗？container的ip是如何实现的？ 


- overlay
    - `--dirver=overlay`

- ingress

- docker shim
- OCI runtime

```
Sending build context to Docker daemon  175.5MB
```


- 一个遇到的问题
    ```
    FROM python:3.9
    COPY osspi-cli .
    WORKDIR /tmp
    CMD ["make"]
    ```
    COPY会失败，原因是 `WORKDIR /tmp` 应该放在 `COPY osspi-cli .` 前面

    - 
    ```
    ---> Running in b7d56f491c28
    /bin/sh: 1: source: not found        <-----
    The command '/bin/sh -c python3.9 -m venv virtualenv &&     source virtualenv/bin/activate &&     pip3.9 install -r requirements.txt &&     pwd' returned a non-zero code: 127

    Reason: source is not sh built-in cmd, it's bash built-in cmd.
    ```
- `If the WORKDIR doesn’t exist, it will be created even if it’s not used in any subsequent Dockerfile instruction`
- `you should use WORKDIR instead of proliferating instructions like RUN cd … && do-something, which are hard to read, troubleshoot, and maintain.`

- docker run --rm
```
在Docker容器退出时，默认容器内部的文件系统仍然被保留，以方便调试并保留用户数据。
但是，对于foreground容器，由于其只是在开发调试过程中短期运行，其用户数据并无保留的必要，因而可以在容器启动时设置--rm选项，这样在容器退出时就能够自动清理容器内部的文件系

显然，--rm选项不能与-d同时使用（或者说同时使用没有意义），即只能自动清理foreground容器，不能自动清理detached容器。
```

- .dockerignore
```
.dockerignore 文件的作用类似于 git 工程中的 .gitignore 。不同的是 .dockerignore 应用于 docker 镜像的构建，它存在于 docker 构建上下文的根目录，用来排除不需要上传到 docker服务端的文件或目录
```


```
# sudo ./virtualenv/bin/activate
/bin/sh: 24: sudo: not found

Solution:

```

- container 中的 terminal 没有自动补全功能的吗？

- docker挂载主机目录 -v 和--mount区别
    - https://zhuanlan.zhihu.com/p/487901733
    - 1. 使用-v时，主机没有这个文件则新建；
    - 2. 使用--mount时，主机没有这个文件则报错。
    - docker run -v 时需要使用 absolute path


#### docker-compose services


#### docker-compose network
- network_mode

- eth 0

- 如何让remote的机器上的端口能被访问，即设置为0.0.0.0这种，在remote上curl http://localhost:5000可以访问，但是curl 类似http://139.196.8.9:5000没用



```
↓ 为什么 PORTS 这列是空的 ？

CONTAINER ID   IMAGE                                                                                        COMMAND                  CREATED          STATUS                  PORTS                                                                                                                                NAMES
ace91934cb7b   internationaldjangoedition_flask                                                             "python app.py runse…"   30 seconds ago   Up 29 seconds                                                                                                                                                internationaldjangoedition_flask_1
c3a63f84aaa5   public.ecr.aws/y5z1i2v3/zhongpengqun:postgres9.6                                             "docker-entrypoint.s…"   31 seconds ago   Up 30 seconds           0.0.0.0:6432->5432/tcp, :::6432->5432/tcp                                                                                            postgresql
```

- docker-compose 只 restart 某个 service, 比如只改了项目的业务逻辑代码，想只restart这部分的某个service
    - $ docker-compose restart websvc

- `a local docker registry`
    - https://www.allisonthackston.com/articles/local-docker-registry
    - docker-registry
        - Docker私服，是存放镜像的本地仓库，类似于docker hub。私服是本地的仓库，用于保存公司内部上传的Docker镜像。

- docker network connect
    - `Connects a container to a network. You can connect a container by name or by ID. Once connected, the container can communicate with other containers in the same network.`



- 如何进入 kubectl get pods中的一个pod ？

```
apt-get update
Reading package lists... Done
E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)
E: Unable to lock directory /var/lib/apt/lists/

-------

```

- --docker-server


- docker/overlay2




$ /usr/bin/dockerd --graph=/media/ubuntu/KINGSTON/docker/lib/docker
unable to configure the Docker daemon with file /etc/docker/daemon.json: EOF
    - /etc/docker/daemon.json is not valid json


```
$ sudo /usr/bin/dockerd --graph=/media/ubuntu/KINGSTON/docker/lib/docker
WARN[2024-03-01T10:53:28.167597399+08:00] The "-g / --graph" flag is deprecated. Please use "--data-root" instead
INFO[2024-03-01T10:53:28.167776048+08:00] Starting up
INFO[2024-03-01T10:53:28.175151306+08:00] detected 127.0.0.53 nameserver, assuming systemd-resolved, so using resolv.conf: /run/systemd/resolve/resolv.conf
failed to start daemon: Unable to get the TempDir under /media/ubuntu/KINGSTON/docker/lib/docker: chown /media/ubuntu/KINGSTON/docker/lib/docker/tmp: operation not permitted


```

- export XDG_RUNTIME_DIR=/home/u/.docker/run
    - 用于指定运行时文件的存储位置

```
denied: requested access to the resource is denied
-------
对要上传的镜像打 Tag，docker tag
```
