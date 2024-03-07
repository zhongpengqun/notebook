---
layout: default
title: Hello
description: Introduction about this site and me.
---

### CS Basic


### Contents
- Python
- Cloud Native
    - Architecture
    - K8S
        - Docker

### Questions
- What's runtime ?

### CNCF

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
    - docker sbom command
    - Configmap
    - 进入pod与进入container的区别？
    - How to get docker disk usage ?  `docker system df`
    - docker export & docker save ?
    - docker import & docker load ?
    - docker export -o english-db-`date +%Y%m%d-%H:%M:%S`.tar c7962a4fee17
    - docker stop then remove all containers
        - `docker stop $(docker ps -aq)`
    - run container from dockerfile
    ```shell
    docker build -t xxx .
    docker run -d xxx
    ```

- Dockerfile
    - USER
    - ARG
    - ENTRYPOINT
    - COPY --chown
    - WORKDIR
    - --build-arg

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

- Docker-compose
- kubectl
  - kubectl create & kubectl apply
  - Services
    - ClusterIp (Default)
    - NodePort
    - 
  - restart: unless-stopped

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
- docker save & docker export

- save docker running container and push to dockerhub
```shell
docker commit 0a887a75b48b centos5.8-pkgs-and-tools-preinstalled:v1
docker tag centos5.8-pkgs-and-tools-preinstalled:v1 zhongpengqun/centos5.8-pkgs-and-tools-preinstalled:v1
docker push zhongpengqun/centos5.8-pkgs-and-tools-preinstalled:v1
```

# docker-compose
- Why `links` ? Is it has any association with `depends_on` ?

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

## K8S
- Run k8s locally
  - Minikube
    - Is it possible for minikube to run 2 clusters on one physical machine ?
      - I guess it's impossible, we use `minikube start` to start a cluster
    - Run a cluster with multiple nodes ?
      - `minikube start --nodes 2 -p multinode-demo`
    - `minikube dashboard`
- What's relationship between Deployment, Pod, Service ?
- kubeadm & kubelet & kubectl
- apiserver & 
- Control plane
- kind notation ?
- `configMapKeyRef`
- k9s
- Comparison of many kinds of k8s local simulate tools, kind, k3s, minikube.
- Nodeport, clusterIP
- Why service ?
- Why ingress ?
- Kustomize VS Helm
  - kustomize yaml
    - resources
    - configMapGenerator
    - patchesStrategicMerge
- Kubectl 内置 Kustomize, 怎么用呢？
- Loadblanch与Ingress的联系？
- services的selector是select pods which label matched，还是select deployments which label matched ?
- 一个pod多个containers，deployment yaml怎么写？
- 一个deployment多个pods怎么写？
- replicat 与 pod是one to one的关系吗？
- Is k8s node a physical computer ?
   - A node can be a physical machine or a virtual machine, and can be hosted on-premises or in the cloud.
- Nginx ingress controller
- namespace
    - get current namespace: `kubectl config get-contexts`
    - switch namespace: `$ kubectl config set-context --current --namespace=kube-ops`
- Cluster
    - How run multi clusters ?
    - How to enter a cluster ?

- kubectl
    - kubectl restart pod `kubectl replace --force -f gitlab-deployment.yaml`

- ConfigMap & secret
- Label, what, why
- How to deploy a flask app to k8s cluster ? speak out
- yaml file changes, how to make it take effect ?
- operator
- Deploy database is different from deploying applications like a Django application.

- Storage
    - Storage Class
    - PV admin

- Stateful
    - Stateless

- Run database in k8s.

- eliminate docker pull limitation
https://www.chenshaowen.com/blog/how-to-cross-the-limit-of-dockerhub.html

- CRD
https://www.youtube.com/watch?v=u1X5Rf7fWwM
- controller
- kind: LimitRange


## Concourse
- What is concourse target, why fly -t (target) ?
- is concourse pipeline yaml file independent of concourse instance ? i mean a yaml file is able to run everywhere.
- groups
- var_sources
- inputs
- reveal: true
- in_parallel
- input_mapping / output_mapping


## Make
- make -p
- make --dry-run
- =,:=,?=
- .PHONY
- firstword， wildcard, patsubst
- include

## Helm
- Install Helm
    - 
- Charts & release
- https://artifacthub.io/


## harbor
https://www.cnblogs.com/gengxiaonuo/p/16840026.html

## Python
- Modules
    - argparse
      - parser.add_mutually_exclusive_group(required=True)
      ```shell
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument(
            '--path',
            dest='path',
            action='append',
        )
        group.add_argument(
            '--folder',
            dest='folder',
            action='store',
        )
      So, argument `--path` & `--folder` must pass one, and not allowed pass two simultaneously.
      ```
    - argparse nargs='+'
    - nargs='*'
    - action='store'
        - action 表示活动，只有在具有触发动作时才显示作用，所以 store_xxx 后面的 xxx（true/false）表示的是触发后的参数值；
        - 所以通常来讲 default=False 和 action='store_true' 会成对出现，default=True 和 action='store_false' 会成对出现 。最终实现既有参数默认赋值功能，又有参数触发切换功能
    ```shell
    self.parser.add_argument(
        "-n",
        dest="dryrun",
        action='store_true', # 一旦有这个参数，做出动作“将其值标为True”,也就是没有时，默认状态下其值为False
        default=False,
        help="xx"
    )
    # 为什么会需要有这种 ↓
    action="store_false",   # store_false也就是默认为True，一旦命令中有此参数，其值则变为False
    default=True,    
    ```

import signal, os

# 定义一个信号处理函数，该函数打印收到的信号，然后raise IOError
def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

# 对SIGALRM(终止)设置处理的handler, 然后设置定时器，5秒后触发SIGALRM信号
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # 关闭定时器
该示例实现的功能是，为了防止打开一个文件出错或者其他异常一直处于等待的状态，设定一个定时器，5秒后触发IOError。如果5s内正常打开文件，则清除定时器。
```

```
parser.add_argument(
    '--test',
    dest='test', default=None, type=int, help='test'
    action='store',     # 
)
```

### python3
from collections.abc import Iterable
typing module, TypedDict
```python
>>> def tt(kk: int, xx: Optional[int]):
...     print(kk)
>>> tt(None)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: tt() missing 1 required positional argument: 'xx'
```

run a simple httpserver
```shell
python3 -m http.server
```

Only compress files in folder, not include this folder.

```shell
tar -czvf python-3.10.6-with-openssl-3.0.5.tar.gz -C python-3.10.6/ .
```

### etcd
- xx

## Owner of this site
- /etc/localtime
- apt-get update
- 动态库 & 静态库
- 向下兼容、向后兼容、向上兼容、向前兼容
## tox
https://tox.wiki/en/latest/

## Jenkins
- Installation
  - xx
- How config github and gitlab project integration ?
- Project types
  - Freestyle Project
    Apply to projects which is simple
  - Pipeline Project
    Apply to projects which more complex, e.g. includes test process, build process    
  - Jenkins manages github repo ?

- Tutorials
    - Complete Jenkins Pipeline Tutorial | Jenkinsfile explained
      https://www.youtube.com/watch?v=7KCS70sCoK0
    - Complete Jenkins Tutorial | Learn Jenkins From Scratch In 3 Hours 🎯| LambdaTest
      https://www.youtube.com/watch?v=nCKxl7Q_20I&t=8610s

## Jira
todo
- transition

### Gitlab & Git
- Installation
 - docker
 - k8s
- gitlab runner
- executor
- tag
- registry
- Git
    - git submodule [Chinese: https://www.youtube.com/watch?v=jhl7ruTPV-o]

## skaffold
https://skaffold.dev

## kustomize
https://kustomize.io/
- patchesStrategicMerge

## Concourse
https://concourse-ci.org/resources.html
- resource_types、resources、var_sources、groups、jobs

- Practice

- minimum_succeeded_builds

## RabbitMQ
- What is channel ? Why channel ?
- Channel is able to basic_consume and basic_publish ?


### POSIX


### Linux
- Kernel Headers
https://unix.stackexchange.com/questions/47330/what-exactly-are-linux-kernel-headers
  - Install kernel headers https://linuxhint.com/install-kernel-headers-debian/
  - History: https://blog.csdn.net/trochiluses/article/details/9390855?spm=1001.2101.3001.6650.14&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-14-9390855-blog-54137564.pc_relevant_3mothn_strategy_and_data_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-14-9390855-blog-54137564.pc_relevant_3mothn_strategy_and_data_recovery&utm_relevant_index=14

### Shell
- bash VS zsh
- Is it possible to write a game by shell script ?
- Makefile
- $(1) means ?
- What does colon do in path ?
- eval
- chmod u+x

### My life and experiences
- Don't integrate other team API which is still on beta, not upgraded on production.
- atomic a series of operations.
- Never hardcode
- Timeout effects user experience

### Software management
<b>What is the Difference Between Build and Release in Software Testing ?</b>

The main difference between Build and Release in Software Testing 

is that Build is a version of a software the development team hands over to the testing team for testing purposes

while Release is a software the testing team hands over to the customer.


<b>what is `deliverable` in software management ?</b>

todo

<b> project vs product </b>

It also leads to another questions

project manager vs product manager
project mindset vs product mindset

<b> inventory </b>

TODO

# Terms
- sandbox, what, why ?

# Angular
- angular vs angularJs
- What's the relationship between angular and Typescript ?

# Typescript
- online playground https://www.typescriptlang.org/play



## Mark
- 2022年09月12日11:17:14


## Shell
```Shell
tar zcvf dist.tar.gz -C dist 
```

```Shell
python3 -m ensurepip
```

Shell 中的 `:=` ?

make all

```shell
ldconfig
```

```
symbolic links & hard links
```

```shell
vzhong@vzhong-vm-2:~/osspi-cli$ sudo ln -s /home/vzhong/osspi-cli/build/resources/openssl/Openssl-3.0.5/lib64/libcrypto.so.3 /usr/lib/libcrypto.so.3
```

```python
vzhong@vzhong-vm-2:~/osspi-cli$ sudo ln -s /home/vzhong/osspi-cli/build/resources/openssl/Openssl-3.0.5/lib64/libssl.so.3 /usr/lib/libssl.so.3
```

```shell
openssl: error while loading shared libraries: libssl.so.3
```


```shell
/usr/bin/install -c /home/vzhong/glibc/glibc-2.36/build/elf/ld.so /lib64/ld-linux-x86-64.so.2.new
mv -f /lib64/ld-linux-x86-64.so.2.new /lib64/ld-linux-x86-64.so.2
rm -f /usr/bin/ld.so.new
Inconsistency detected by ld.so: dl-call-libc-early-init.c: 37: _dl_call_libc_early_init: Assertion `sym != NULL' failed!
Makefile:1390: recipe for target '/usr/bin/ld.so' failed
make[2]: *** [/usr/bin/ld.so] Error 127
make[2]: Leaving directory '/home/vzhong/glibc/glibc-2.36/elf'
Makefile:484: recipe for target 'elf/subdir_install' failed
make[1]: *** [elf/subdir_install] Error 2
make[1]: Leaving directory '/home/vzhong/glibc/glibc-2.36'
Makefile:12: recipe for target 'install' failed
make: *** [install] Error 2
```


```shell
Inconsistency detected by ld.so: dl-call-libc-early-init.c: 37: _dl_call_libc_early_init: Assertion `sym != NULL' failed!
```




## 2022年09月13日12:50:10
```python
subprocess.check_output(cmd, shell=True, text=True)
```

## 2022年09月14日16:42:30
linux install docker-compose

```shell
https://github.com/docker/compose/releases/tag/v2.10.2
https://github.com/docker/compose/releases/download/v2.10.2/docker-compose-linux-x86_64
```

2022年09月15日11:06:08
```shell
docker-compose stop & docker-compose down
```

Rebuild and restart container

```shell
docker-compose up --detach --build gunicorn
docker-compose up --build gunicorn
```

```
Referer is insecure while host is secure
```

2022年09月16日11:53:20
```shell

```

2022年09月19日13:40:15

```python
>>> 'http://xx.com'.lstrip('xhttfffff://p')
'.com'
```

```shell
# ./restart.sh
Error response from daemon: client and server don't have same version (client : 1.24, server: 1.18)
[+] Building 0.0s (0/0)                                                                                                                  
Error response from daemon: client and server don't have same version (client : 1.24, server: 1.18): driver not connecting
Error response from daemon: client and server don't have same version (client : 1.24, server: 1.18)
```

scrum与waterfall，难道不是只是粒度变细了吗？

2022年09月20日10:09:50

```shell
curl --unix-socket /var/run/docker.sock http://localhost/version
```

- ingress-nginx

install docker on ubuntu
```shell
apt-get install docker.io
```

```shell
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7EA0A9C3F273FCD8
```

Crash & Crush

differences between `helpnow` and `servicedesk`


```shell
pytest tox.ini lint
```

## Software test

```shell
coverage run --branch --source=. --omit=*/tests*,*__init__* -m unittest discover
```

---------
https://www.bilibili.com/video/BV1LD4y1o79K/?spm_id_from=autoNext&vd_source=f209dde1a1d76e06b060a034f36bb756

https://www.gutenberg.org/files/1998/1998-h/1998-h.htm

https://www.gutenberg.org/files/1998/1998-h/1998-h.htm#link2H_INTR

2022年09月21日10:49:03

- test --> side effect

- How coverage test a specific case ?

```python
>>> try:
...     assert 1==2
... except Exception as exc:
...     print(str(exc))
...

>>>
```

--------------------
2022年10月09日15:21:06

`LD_RUN_PATH和LD_LIBRARY_PATH是干什么的?`

module from so file ?
```python
>>> import _tkinter
>>>
>>> _tkinter
<module '_tkinter' from '/usr/local/python-3.10.6-with-openssl-3.0.5/lib/python3.10/lib-dynload/_tkinter.cpython-310-x86_64-linux-gnu.so'>
>>>
```

2022年09月22日14:01:09

- How do I run a docker instance from a DockerFile?

2022年09月23日13:50:44

github
```shell
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/zhongpengqun/mirror.git/'
```
s: https://stackoverflow.com/questions/68775869/message-support-for-password-authentication-was-removed-please-use-a-personal


2022年09月26日15:31:05

- echo $(PWD) 啥都没有..


- self-contained

- 沟通技巧

2022年09月27日15:25:27
- 动态库与静态库

2022年09月30日10:34:26

- what's standard output standard input ?

2022年10月04日09:14:39

- echo $?


### Work
  - [Note](./note.html)
  - 技术选型怎么做?
  - 如何熟悉新项目    /自问自答
  - Professional
    - 计算机组成原理 
      - 科学计数法 & 浮点数
  - Project details understanding
  - [K8s studying](./k8s-studying.html)
  - Django-rest-framework
      - 2种url参数的区别，为什么要这样？
  - RabbitMQ
  - JIRA
  - Django
      - safe url
      - url endswith '/' & not endswith
      - Path Parameters
      - setup project from legacy database
      - ALLOWED_HOSTS
        - HTTP Host header attacks
  - Python
      - python 3
      - logging
      - urllib urlparse
      -         "message": "Dangerous default value {} as argument",
      - super 放在不同的位置会怎样？
      - when staticmethod, when classmethod ?
      - collections
      - array & list
        - https://medium.com/backticks-tildes/list-vs-array-python-data-type-40ac4f294551
      - lambda, filter
  - Git
      - Git branch strategy
  - Society studying & Social practice
    - Laws of the People's Republic of China
  - OS
    - Lock
    - linux cpio
  - Remote edit
  - [Software Life Circle](./software-life-circle.html)
  - [Angular](./angular.html)
  - code snippet
  - The experience of using grafana

## Study
  - [English Studying](./english-studying.html)
  - [Translation](./translation.html)
  - Linux 0.0.1

  - Road traffic laws and rules
    - [Motorcycles i might buy](./motorcycles.html)

  - English Reading Notes
    - Thus spoke Zarathustra
    - https://www.quora.com/Did-Nietzsche-have-any-dark-secrets
    - [The Communist Manifesto](./the-communist-manifesto.html)





### PyInstaller
- .spec file
```python
# 
configuration = Analysis(['moccasin/__main__.py'],
                         pathex = ['.'],
                         binaries = [(libsbml_lib_path(), '.')],
                         datas = [],
                         hiddenimports = [],
                         hookspath = [],
                         runtime_hooks = [],
                         excludes = [],
                         win_no_prefer_redirects = False,
                         win_private_assemblies = False,
                         cipher = None,
                        )

application_pyz    = PYZ(configuration.pure,
                         configuration.zipped_data,
                         cipher = None,
                        )

executable         = EXE(application_pyz,
                         configuration.scripts,
                         configuration.binaries,
                         configuration.zipfiles,
                         configuration.datas,
                         name = 'moccasin',
                         debug = False,
                         strip = False,
                         upx = True,
                         runtime_tmpdir = None,
                         console = False,
                        )

app             = BUNDLE(executable,
                         name = 'MOCCASIN.app',
                         icon = 'dev/icon/moccasin.icns',
                         bundle_identifier = None,
                         info_plist = {'NSHighResolutionCapable': 'True'},
                        )
```


### mess
- What does inline mean ?


- https://www.cnblogs.com/god-of-death/p/12767113.html

- Splunk
    - https://www.youtube.com/watch?v=m95GiTF0zd0
    - https://www.youtube.com/watch?v=bO_-fv6e7u4
    - https://medium.com/airwalk/log-aggregation-in-kubernetes-and-transporting-logs-to-splunk-for-analysis-ad8599607372
    - https://cloud.google.com/architecture/logging-anthos-with-splunk-connect?hl=zh-cn
    - k8s logs
        - objects
        - metrics


setup a splunk server:
```shell
docker run --name splunk -p 8000:8000 -p 8088:8088 -d outcoldman/splunk:6.3.3


docker run --name hello --log-driver=splunk --log-opt splunk-token=022F1FCE-B904-4E0E-B0A1-EB4492F61B9D --log-opt splunk-url=http://139.196.39.92:8088 --log-opt splunk-sourcetype=Docker rickfast/hello-oreilly


docker run --name hello --log-driver=splunk --log-opt splunk-token=A3260AEC-672D-41D2-9B64-8BAB933EA5DE --log-opt splunk-url=http://139.196.39.92:8088 --log-opt splunk-sourcetype=Docker rickfast/hello-oreilly



docker run --name hello --log-driver=splunk --log-opt splunk-token=1620a639-5064-43dc-8d81-72ae38ec639b --log-opt splunk-url=http://10.79.128.59:8088 --log-opt splunk-sourcetype=Docker rickfast/hello-oreilly

minikube start --nodes 4 --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 1

minikube start --nodes 4 --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 1 --driver=docker
```





```shell
curl -k https://139.196.39.92:8088/services/collector/event -H "Authorization: Splunk C8D04ABF-AE0A-4FEB-935C-9F0751FEA816" -d '{"event": "hello world"}'
```

splunk log success: https://www.youtube.com/watch?v=qROXrFGqWAU&t=11s

curl https://10.79.128.59:8088/services/collector/event -H "Authorization: Splunk 1620a639-5064-43dc-8d81-72ae38ec639b" -d '{"event": "hello world"}'

docker built-in send log to splunk ?
https://www.w3cschool.cn/doc_docker_1_13/docker_1_13-engine-admin-logging-splunk-index.html

install splunk by cmd
https://www.inmotionhosting.com/support/security/install-splunk/

9ED0A79E-F7B8-43DC-B7A0-7B49AE7450B9

```shell
root@iZuf6bpc1lt9qlf2ma9p2lZ:~# helm install anthos-splunk -f values.yaml --namespace splunk-connect https://github.com/splunk/splunk-connect-for-kubernetes/releases/download/1.4.1/splunk-connect-for-kubernetes-1.4.1.tgz

Error: INSTALLATION FAILED: Get "https://github.com/splunk/splunk-connect-for-kubernetes/releases/download/1.4.1/splunk-connect-for-kubernetes-1.4.1.tgz": unexpected EOF
```

- [back](./)


gcc - https://blog.csdn.net/lailaiquququ11/article/details/126691913


```shell
$ kubectl create namespace splunk-connect
$ kubectl config set-context --current --namespace=splunk-connect
$ 
helm install anthos-splunk -f values.yaml --namespace splunk-connect https://github.com/splunk/splunk-connect-for-kubernetes/releases/download/1.4.1/splunk-connect-for-kubernetes-1.4.1.tgz
```

```shell
Exiting due to RSRC_INSUFFICIENT_CORES: Requested cpu count 2 is greater than the available cpus of 1

minikube start --nodes 4 --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 1
```


阿里云 1GB memeory, 1 cpu
k3s失败, minikube 资源不足
kind success

- xrdb
- 
- build-essential

### Fabric


### Vmware
- vSphere
- vSan
- esx, esxi, NFS, ISCSI



### Legal
- Copyleft



```shell
# mhsendmail -h
Segmentation fault
```


### Django doc notes
```
https://www.django-rest-framework.org/api-guide/serializers/

Expanding the usefulness of the serializers is something that we would like to address. However, it's not a trivial problem, and it will take some serious design work
扩展序列化程序的有用性是我们想要解决的问题。然而，这不是一个微不足道的问题，它需要一些认真的设计工作
```

- django serializer & drf serializer
- what should a serializer be ? i mean how to design a suitable serializer ?



#### jekyll
```shell
docker run -it  --rm jekyll/jekyll:3.5 bash

bundle exec jekyll serve

# gem sources -a http://gems.ruby-china.org
Error fetching http://gems.ruby-china.org:
        no such name (http://gems.ruby-china.org/specs.4.8.gz)



install ruby in ubuntu18.04 container by source code
https://tool.4xseo.com/article/501208.html
```


```shell
# kubectl get pods
The connection to the server localhost:8080 was refused - did you specify the right host or port?

[resolve] https://blog.csdn.net/a506681571/article/details/86086005

systemctl start etcd
systemctl start docker
systemctl start kube-apiserver
systemctl start kube-controller-manager
systemctl start kube-scheduler
systemctl start kubelet
systemctl start kube-proxy
----------------

# docker-compose up -d
[+] Running 0/0
 ⠿ Network concourse_default  Error                                                                                                                                        0.0s
failed to create network concourse_default: Error response from daemon: Failed to Setup IP tables: Unable to enable SKIP DNAT rule:  (iptables failed: iptables --wait -t nat -I DOCKER -i br-7b98d6e4dcfd -j RETURN: iptables: No chain/target/match by that name.
 (exit status 1))

[resolved]
# systemctl restart docker.service
# docker-compose up -d
```


https://github.com/joeltennant/Jekyll-and-Docker-Compose
```shell
# docker-compose up
[+] Running 2/2
 ⠿ Network jekyll-and-docker-compose_default     Created                                                                                                                                               0.0s
 ⠿ Container jekyll-and-docker-compose-jekyll-1  Created                                                                                                                                               0.1s
Attaching to jekyll-and-docker-compose-jekyll-1
jekyll-and-docker-compose-jekyll-1  | ruby 3.1.1p18 (2022-02-18 revision 53f5fc4236) [x86_64-linux-musl]
jekyll-and-docker-compose-jekyll-1  |   Logging at level: debug
jekyll-and-docker-compose-jekyll-1  |     Jekyll Version: 4.2.2
jekyll-and-docker-compose-jekyll-1  | Configuration file: /srv/jekyll/_config.yml
jekyll-and-docker-compose-jekyll-1  |   Logging at level: debug
jekyll-and-docker-compose-jekyll-1  |     Jekyll Version: 4.2.2
jekyll-and-docker-compose-jekyll-1  |                     ------------------------------------------------
jekyll-and-docker-compose-jekyll-1  |       Jekyll 4.2.2   Please append `--trace` to the `serve` command 
jekyll-and-docker-compose-jekyll-1  |                      for any additional information or backtrace. 
jekyll-and-docker-compose-jekyll-1  |                     ------------------------------------------------
jekyll-and-docker-compose-jekyll-1  | /usr/local/lib/ruby/3.1.0/fileutils.rb:243:in `mkdir': Permission denied @ dir_s_mkdir - /srv/jekyll/.jekyll-cache (Errno::EACCES)
jekyll-and-docker-compose-jekyll-1  |   from /usr/local/lib/ruby/3.1.0/fileutils.rb:243:in `fu_mkdir'
jekyll-and-docker-compose-jekyll-1  |   from /usr/local/lib/ruby/3.1.0/fileutils.rb:221:in `block (2 levels) in mkdir_p'
jekyll-and-docker-compose-jekyll-1  |   from /usr/local/lib/ruby/3.1.0/fileutils.rb:219:in `reverse_each'
jekyll-and-docker-compose-jekyll-1  |   from /usr/local/lib/ruby/3.1.0/fileutils.rb:219:in `block in mkdir_p'
jekyll-and-docker-compose-jekyll-1  |   from /usr/local/lib/ruby/3.1.0/fileutils.rb:211:in `each'
jekyll-and-docker-compose-jekyll-1  |   from /usr/local/lib/ruby/3.1.0/fileutils.rb:211:in `mkdir_p'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/cache.rb:184:in `dump'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/cache.rb:101:in `[]='
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/cache.rb:45:in `clear_if_config_changed'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/site.rb:118:in `reset'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/site.rb:35:in `initialize'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/commands/build.rb:30:in `new'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/commands/build.rb:30:in `process'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/command.rb:91:in `block in process_with_graceful_fail'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/command.rb:91:in `each'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/command.rb:91:in `process_with_graceful_fail'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/commands/serve.rb:86:in `block (2 levels) in init_with_program'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `block in execute'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `each'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `execute'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/mercenary-0.4.0/lib/mercenary/program.rb:44:in `go'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/mercenary-0.4.0/lib/mercenary.rb:21:in `program'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/exe/jekyll:15:in `<top (required)>'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/bin/jekyll:25:in `load'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/bin/jekyll:25:in `<main>'
jekyll-and-docker-compose-jekyll-1 exited with code 1
```


### Alpine Linux