### todo，不错的博客
- https://jimmysong.io/kubernetes-handbook/concepts/taint-and-toleration.html

###
- 容器引擎


### q
- 什么规模的公司适合用k8s?



### K8S
- Todos
    - https://www.bilibili.com/video/BV1pT4y1C7Em/?spm_id_from=333.337.search-card.all.click
    - https://www.bilibili.com/video/BV14P4y1P7uN/?spm_id_from=333.337.search-card.all.click

    - k8s生态，有哪些工具是必要的
    - sealos

- 所有resource type，以及types之间的关系，比如包含，平级
  - namespace是一种type吗？

- 扩展Kubernetes API
  - 什么时候有必要？

- k8s 集群的日志收集
  - FLUENTD收集K8S集群日志:  https://www.cnblogs.com/windchen/p/12924091.html      todo: 实践一下，demo一下
  - 一种方案：fluentd + elastic search + Kibaba
  ```
  在本文中采用使用Node日志记录代理的方面进行Kubernetes的统一日志管理，相关的工具采用：

  日志记录代理（logging-agent）：日志记录代理用于从容器中获取日志信息，使用Fluentd；
  日志记录后台（Logging-Backend）：日志记录后台用于处理日志记录代理推送过来的日志，使用Elasticsearch；
  日志记录展示：日志记录展示用于向用户显示统一的日志信息，使用Kibana。
  ```

- emptyDir
	- 应用场景
		- emptyDir Volume主要用于某些应用程序无需永久保存的临时目录，多个容器的共享目录等。

- 说到cluster的时候，是指namespace specified的cluster还是整个k8s cluster ？
```
1: What is a Kubernetes namespace?

A Kubernetes namespace is a virtual cluster within a Kubernetes cluster that provides a way to organise resources and isolate them from other resources in the cluster.
```

- Run k8s locally
  - Minikube
    - Is it possible for minikube to run 2 clusters on one physical machine ?
      - I guess it's impossible, we use `minikube start` to start a cluster
    - Run a cluster with multiple nodes ?
      - `minikube start --nodes 2 -p multinode-demo`
    - `minikube dashboard`
      - 和 k8s dashboard 是一个东西吗？
- 为什么docker ps不会显示出k8s里的containers ？如何看k8s里的containers?
- What's relationship between Deployment, Pod, Service ?
  - 
  ```
  举例来说有一个 Deployment 控制器管控值集群里的一组 Pod，当你 Kill 掉一个 Pod。控制器发现定义中期望的 Pod 数量与当前的数量不匹配，它就会马上创建一个 Pod 让当前状态与期望状态匹配。控制器这种让关联资源的当前状态向期望状态迈进的过程叫做 调谐（reconcile）。
  ```
  - 5种控制器
- kubeadm & kubelet & kubectl
  - kubectl 是否只能用在k8s中
  - k8s是否只有kubectl这一个东西来apply它的yaml file ?
  - `docker ps`命令是否能显示k8s中的container ？
- apiserver & 
- Control plane
- kind notation ?
- `configMapKeyRef`
- k9s
- Comparison of many kinds of k8s local simulate tools, kind, k3s, minikube.
- ClusterIP, Nodeport, LoadBalancer, Ingress
  - ClusterIP 服务是 Kubernetes 的默认服务。它给你一个集群内的服务，集群内的其它应用都可以访问该服务。集群外部无法访问它
    - 如果 从Internet 没法访问 ClusterIP 服务，那么我们为什么要讨论它呢？那是因为我们可以通过 Kubernetes 的 proxy 模式来访问该服务

    启动 Kubernetes proxy 模式：
    $ kubectl proxy --port=8080 
    这样你可以通过Kubernetes API，使用如下模式来访问这个服务：

    http://localhost:8080/api/v1/proxy/namespaces/<NAMESPACE>/services/<SERVICE-NAME>:<PORT-NAME>/ 
    要访问我们上面定义的服务，你可以使用如下地址：

    http://localhost:8080/api/v1/proxy/namespaces/default/services/my-internal-service:http/ 
    何时使用这种方式？

    有一些场景下，你得使用 Kubernetes 的 proxy 模式来访问你的服务：

    由于某些原因，你需要调试你的服务，或者需要直接通过笔记本电脑去访问它们。
    容许内部通信，展示内部仪表盘等。
    这种方式要求我们运行 kubectl 作为一个未认证的用户，因此我们不能用这种方式把服务暴露到 internet 或者在生产环境使用。

  - Nodeport
    - NodePort 服务是引导外部流量到你的服务的最原始方式。NodePort，正如这个名字所示，在所有节点（虚拟机）上开放一个特定端口，任何发送到该端口的流量都被转发到对应服务
    - 何时使用这种方式？

      这种方法有许多缺点：
      每个端口只能是一种服务
      端口范围只能是 30000-32767
      如果节点/VM 的 IP 地址发生变化，你需要能处理这种情况

      基于以上原因，我不建议在生产环境上用这种方式暴露服务。如果你运行的服务不要求一直可用，或者对成本比较敏感，你可以使用这种方法。`这样的应用的最佳例子是 demo 应用，或者某些临时应用`

  - LoadBalancer
    - LoadBalancer 服务是暴露服务到 internet 的标准方式
    - 这种服务是云服务器厂商提供的吗？
      - 盲猜应该是的
    - 它没有过滤条件，没有路由等。这意味着你几乎可以发送任何种类的流量到该服务，像 HTTP，TCP，UDP，Websocket，gRPC 或其它任意种类。
    这个方式的最大缺点是每一个用 LoadBalancer 暴露的服务都会有它自己的 IP 地址，每个用到的 LoadBalancer 都需要付费，这将是非常昂贵的。

  - Ingress
    - Why ingress ?
    - ingress-nginx
    - Nginx ingress controller
    - Loadblanch与Ingress的联系？
    - Ngnix与ingress的关系？

    - Ingress 可能是暴露服务的最强大方式，但同时也是最复杂的。Ingress 控制器有各种类型，包括 Google Cloud Load Balancer， Nginx，Contour，Istio，等等。它还有各种插件，比如 cert-manager[5]，它可以为你的服务自动提供 SSL 证书。



- Why service ?

- Kustomize VS Helm
  - kustomize yaml
    - resources
    - configMapGenerator
    - patchesStrategicMerge
  - `个人觉得 Kustomize 更适合做 gitops 而 helm 更合适做应用包的分发。`
- Kubectl 内置 Kustomize, 怎么用呢？
- services的selector是select pods which label matched，还是select deployments which label matched ?
- 一个pod多个containers，deployment yaml怎么写？
- 既然pod是k8s调度的最小单位,kubectl有操作container相关的命令吗？
  - 一个pod里可能有多个containers，对吧？
- 一个deployment多个pods怎么写？
- replicat 与 pod是one to one的关系吗？
- Is k8s node a physical computer ?
   - A node can be a physical machine or a virtual machine, and can be hosted on-premises or in the cloud.
- namespace
    - get current namespace: `kubectl config get-contexts`
    - switch namespace: `$ kubectl config set-context --current --namespace=kube-ops`
- Cluster
    - How run multi clusters ?
    - How to enter a cluster ?
- Job
f.e.
```shell
apiVersion: batch/v1
kind: Job
metadata: 
  name:
  namespace:
  labels:
    controller: job
spec:
  completions: 1  #指定job需要成功运行pods的次数，默认值为1
  parallelism: 1  #指定job在任一时刻应该并发运行pods的数量，默认值为1
  activeDeadlineSeconds: 30  #指定job可运行的时间期限，超过时间还未结束，系统将会尝试进行终止
  backoffLimit: 6  #指定job失败后进行重试的次数，默认值是6
  manualSelector: true  #是否可以使用selector选择器选择pod，默认是false
  selector: #选择器，通过它指定该控制器管理哪些pod
    matchLabels:  #Labels匹配规则
      app: counter-pod
    matchExpressions:  #Expression匹配规则
      - {key: app, operator: In, values: [counter-pod]}
  template:  #模板，当副本数量不足时，会根据下面的模板创建pod副本
    metadata: 
      labels:
        app: counter-pod
    spec:
      restartPolicy: Never  #重启策略只能设置为Never或者OnFailure
      containers:
      - name: counter
        image: busybox:1.30
        command: ["bin/sh","-c","for i in 9 8 7 6 5 4 3 2 1;do echo $i;sleep 2;done"]
```
- kubectl
    - kubectl restart pod `kubectl replace --force -f gitlab-deployment.yaml`
    - kubectl能查看pod里的container吗？

- 如何在k8s里跑一个hello-world?

- k8s权限配置（ServiceAccount、Role、ClusterRole）
  - https://www.youtube.com/watch?v=oBf5lrmquYI
    - 10 best practise on security
      - RBAC
    - K10
  - ServiceAccount
  - https://octopus.com/blog/k8s-rbac-roles-and-bindings

- kind: Endpoints
  - https://developer.aliyun.com/article/530966
  ```
  在之前的博文中，我们演示过如何通过ceph来实现kubernetes的持久存储，以使得像mysql这种有状态服务可以在kubernetes中运行并保存数据。这看起来很美妙，然而在实际的生产环境使用中，通过分布式存储来实现的磁盘在mysql这种IO密集性应用中，性能问题会显得非常突出。所以在实际应用中，一般不会把mysql这种应用直接放入kubernetes中管理，而是使用专用的服务器来独立部署。而像web这种无状态应用依然会运行在kubernetes当中，这个时候web服务器要连接kubernetes管理之外的数据库，有两种方式：一是直接连接数据库所在物理服务器IP，另一种方式就是借助kubernetes的Endpoints直接将外部服务器映射为kubernetes内部的一个服务.
  ```

- k8s cluster ip ?

- ConfigMap & secret
  - k8s 还有哪些方式去挂载配置文件？
  - refer: https://www.jianshu.com/p/d834bca35c18

  - ConfigMap
    - https://www.jianshu.com/p/d834bca35c18
    应用部署的一个最佳实践是将应用所需的配置信息与程序进行分离，这样可以使得应用程序被更好地复用，通过不同的配置也能实现更灵活的功能。
    将应用打包为容器镜像后，可以通过环境变量或者外挂文件的方式在创建容器时进行配置注入，但在大规模容器集群的环境中，对多个容器进行不同的配置将变得非常复杂。
    从Kubernetes v1.2开始提供了一种统一的应用配置管理方案——ConfigMap
    2:
    在我们部署一些应用服务时，通常都会有一些配置文件，而在k8s中，我们如果在将这些配置文件写到代码应用程序中，需要修改配置的话，我们还得重新去修改代码，重新制作一个镜像，这样操作起来很麻烦。

  - secret
    - 一般情况下ConfigMap 是用来存储一些非安全的配置信息，因为ConfigMap是明文存储的，面对敏感信息时，我们就需要使用k8s的另一个对象Secret。

- Yaml file command字段, args字段，Dockerfile中ENTRYPOINT和CMD，生效顺序

- Label, what, why
- How to deploy a flask app to k8s cluster ? speak out
- yaml file changes, how to make it take effect ?
- operator
  - 正如官方 Kubernetes 文档所说，“Operators 是 Kubernetes API 的客户端，充当自定义资源的控制器”
  - kubebuilder、operator-sdk
  - 为什么需要operator, operator是k8s官方的吗？
    - k8s的文档中本身没有operator这个词
  - k8s operator 开发
    - 通过自己编写Controller来不断地检测当前k8s中所定义的CR的状态，如果状态和预期不一致，则调整
  - TODO: 最小demo
- CRD
  - why?

  - `ensure CRDs are installed first`
  - https://www.youtube.com/watch?v=u1X5Rf7fWwM

- Deploy database is different from deploying applications like a Django application.

- Storage
  - K8S local storage
  - Storage Class
  - PV admin

- Stateful
    - why?
    - Stateless

- Run database in k8s.

- crontab
  - CronJob 也可以用来指定将来某个时间点执行单个任务，例如将某项任务定时到系统负载比较低的时候执行

- eliminate docker pull limitation
https://www.chenshaowen.com/blog/how-to-cross-the-limit-of-dockerhub.html


- controller
- kind: LimitRange


- DaemonSet
  - 每个node只能有一个daemonset
  `Splunk Connect for Kubernetes deploys a DaemonSet on each node, And in the DaemonSet, a Fluentd container runs and does the collecting job.`
  - DaemonSet是一个pod吗？
    - yes
  - 编写go项目daemonset来清理k8s节点上的磁盘空间   https://www.bilibili.com/video/av347091144/
  - DaemonSet的典型应用场景有
    - 1,运行存储Daemon
      - 比如 分布式存储 glusteFS 或 ceph
    - 2,运行日志收集Daemon
      - 比如 flunentd 或 logstash
    - 3,运行监控Daemon
      - 比如 Prometheus Node Exporter 或 collectd
  - 其实Kubernetes自己就在用DaemonSet运行系统组件
  - 查看所有的DaemonSet
    - kubectl get daemonset


- node logging agent
- Kubernetes objects
- Kubernetes Components

- Taints & Tolerations
  - https://kubernetes.io/zh-cn/docs/concepts/scheduling-eviction/taint-and-toleration/
  - https://www.google.com/search?q=k8s+taint&biw=1859&bih=953&tbm=vid&sxsrf=APwXEde21b3AthbfDN74B5_h0vdEx0Myyg%3A1679905599446&ei=P1MhZLneGqS8seMPkeyo4Ac&ved=0ahUKEwj5-YqE2Pv9AhUkXmwGHRE2CnwQ4dUDCA0&uact=5&oq=k8s+taint&gs_lcp=Cg1nd3Mtd2l6LXZpZGVvEAMyBQgAEIAEMggIABCABBDLATIICAAQgAQQywEyBQgAEIAEMggIABCKBRCGAzIICAAQigUQhgMyCAgAEIoFEIYDOgQIIxAnOgYIABAWEB46BwgAEIoFEEM6CAgAEIoFEJECOgsIABCKBRCxAxCDAToLCAAQgAQQsQMQgwE6BAgAEB46BggAEB4QCjoGCAAQBRAeOgUIABCiBDoHCCMQ6gIQJzoKCAAQigUQsQMQQ1CuD1j_JGD5J2gFcAB4AIABuQGIAZ4LkgEDMC45mAEAoAEBoAECsAEKwAEB&sclient=gws-wiz-video#fpstate=ive&vld=cid:b29dc380,vid:mo2UrkjA7FE
  - 应用场景
    - https://www.youtube.com/watch?v=rFYqUxjg_5Y
  - xx
  ```
  我们说到的的NodeAffinity节点亲和性，是在pod上定义的一种属性，使得Pod能够被调度到某些node上运行。Taint刚好相反，它让Node拒绝Pod的运行。
  Taint需要与Toleration配合使用，让pod避开那些不合适的node
  ```

- 亲和度

- pod & container
  - pod的log有吗？在哪可以看？

  - https://www.youtube.com/watch?v=5cNrTU6o3Fw
  - 
  ```
  查看Pod，REDY为2/2，表示这个Pod的两个容器都成功运行了。
  [root@node2 test]# kubectl get pods | grep redis-php
  redis-php            2/2     Running   0          3m
  ```
  - enter a pod ?
    - https://stackoverflow.com/questions/67550782/how-to-login-enter-in-kubernetes-pod
    - $ kubectl exec webserver-f848cb844-dvpjk -it -- /bin/sh
      - ↑ 为什么一个pod可以以这种方式进入？
        - 这种方式和docker exec类似，说明pod是k8s的基本调度单元吧，pod之于cluster，类似container之于docker，我的想法
      - 确实是make sense的吧，就像是一个host，container是其中的process

  - 如何查看pod中不同的container的log ？
  - 能否进入pod中的container ？

- kail
  - 可以查看pod的实时日志
  - 对比 kubectl logs有什么优势呢？

### minikube
```shell
minikube start --nodes 4 --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 2 --driver=docker
```

```shell
Exiting due to RSRC_INSUFFICIENT_CORES: Requested cpu count 2 is greater than the available cpus of 1

minikube start --nodes 4 --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 1
```

```shell
$ minikube start --nodes 4 --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 2 --driver=docker

其中报了一个如下的错误：
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
Here is one example how you may list all running Kubernetes containers by using crictl:
        - 'crictl --runtime-endpoint unix:///var/run/cri-dockerd.sock ps -a | grep kube | grep -v pause'
        Once you have found the failing container, you can inspect its logs with:
        - 'crictl --runtime-endpoint unix:///var/run/cri-dockerd.sock logs CONTAINERID'

stderr:
W0212 19:34:22.649439   15157 initconfiguration.go:119] Usage of CRI endpoints without URL scheme is deprecated and can cause kubelet errors in the future. Automatically prepending scheme "unix" to the "criSocket" with value "/var/run/cri-dockerd.sock". Please update your configuration!
        [WARNING SystemVerification]: failed to parse kernel config: unable to load kernel module: "configs", output: "modprobe: FATAL: Module configs not found in directory /lib/modules/5.15.0-56-generic\n", err: exit status 1
        [WARNING Service-Kubelet]: kubelet service is not enabled, please run 'systemctl enable kubelet.service'
error execution phase wait-control-plane: couldn't initialize a Kubernetes cluster
To see the stack trace of this error execute with --v=5 or higher

于是我执行 `systemctl enable kubelet.service`, but got:
Failed to enable unit: Unit file kubelet.service does not exist.

then try another approach: add `--kubernetes-version=v1.23.1`
$ minikube start --nodes 2 --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 2 --kubernetes-version=v1.23.1
succeed !!
```


- cgroup driver
    - `k8s 的是systemd，而docker是cgroupfs`

- Container systemd

- kubectl delete pod,删完后又发现重启了
  - 删除对应的deployment
    - 但是一个pod也有可能是daemonset
  - 如何找到pod对应的deployment ？


- kind: StatefulSet

- https://artifacthub.io/

```shell
# kubectl get pods
NAME                                                READY   STATUS             RESTARTS       AGE
hello-world-deployment-6b8dbb9c94-2vxpn             1/1     Running            0              43m
hello-world-deployment-6b8dbb9c94-mj766             1/1     Running            0              44m
my-splunk-connect-splunk-kubernetes-logging-dvsb8   1/1     Running            1 (44m ago)    16d
my-splunk-connect-splunk-kubernetes-logging-jhdzc   0/1     CrashLoopBackOff   13 (82s ago)   16d
my-splunk-connect-splunk-kubernetes-logging-krlp4   1/1     Running            1 (45m ago)    16d
my-splunk-connect-splunk-kubernetes-logging-zfbqr   1/1     Running            1 (44m ago)    16d

其中 'hello-world-deployment-6b8dbb9c94-2vxpn' 是pod还是container？
```


#### minikube




#### kubectl
- kubectl port-forward
```
若pod内服务没有通过service对外暴露的话，无法去调试pod内的服务，不方便。因此就有了 kubectl port-forward 这个功能。
可以把 Node 主机端口 转发 到 pod 内某个端口

# Listen on port 8888 locally, forwarding to 5000 in the pod
kubectl port-forward pod/mypod 8888:5000

# Listen on a random port locally, forwarding to 5000 in the pod
kubectl port-forward pod/mypod :5000
```



- ready 0/1
```shell
# kubectl get pods
NAME                             READY   STATUS        RESTARTS   AGE
elasticsearch-master-0           0/1     Terminating   0          61m
elasticsearch-master-1           0/1     Pending       0          6h51m
elasticsearch-master-2           0/1     Pending       0          176m
kibana-kibana-77656d9cdd-xt4m2   0/1     Running       0          6h50m
```

  - What's the meaning of "READY=2/2" output by command "kubectl get pod"
    - one pod contains 2 containers, 2 are ready.

- /run/secrets/kubernetes.io/serviceaccount

- one cluster vs many clusters
  - why multi clusters, when we need it?
  - multi clusters locally deploy
  - multi clusters management
  - 默认有multi clusters吗？还是只是其他公司实现的一套黑科技
  - is it possible and nesscary that clusters communicate with each other ?
  - todos
    - https://www.qovery.com/blog/kubernetes-multi-cluster-why-and-when-to-use-them


- kube-system


```
  accessModes:
    - ReadWriteMany  # the volume can be mounted as read-write by many nodes.

  annotations:
    external-dns.alpha.kubernetes.io/hostname:
```

- Kubernetes 101: Pods, Nodes, Containers, and Clusters
  - https://medium.com/google-cloud/kubernetes-101-pods-nodes-containers-and-clusters-c1509e409e16
    - `A node is the smallest unit of computing hardware in Kubernetes.`
    - `Pods are used as the unit of replication in Kubernetes`
    - `Any containers in the same pod will share the same resources and local network.`
      - `pods should remain as small as possible, typically holding only a main process and its tightly-coupled helper containers`

- 同一个node上部署2个相同的pod，有必要吗，有何优势？
  - https://stackoverflow.com/questions/69897258/advantage-of-multiple-pod-on-same-node

- Kubernetes as a service
  - k8s on-premise
  - 本地磁盘当做 data-center
  - https://komodor.com/learn/kubernetes/
    - `Kubernetes can be deployed in all public clouds and also in a local data center, creating a private cloud.`
  - What is Kubernetes multi-cluster?
    - https://www.mirantis.com/cloud-native-concepts/getting-started-with-kubernetes/what-is-kubernetes-multi-cluster/
      - `These clusters may be on the same physical host, on different hosts in the same data center, or even in different clouds in different countries, for a multi-cloud environment.`

- Namespace resources
  - 
  - 如果Deployment 中的 replicas 是2，那么namespcae所需的resource会 x2 吗？
  - how to calculate k8s namespace required resource from deployment yaml file
  - replicas: 0
  

- Why Kustomize is better than Helm?

```
kustomize: cannot execute binary file: Exec format error
可能是下载的tar与系统不兼容，换一个tar下载
```

- `kustomize edit add base`
  - can run `kustomize edit add` to see help text

- kustomize edit add secret fk --disableNameSuffixHash --from-file=./secrets/xx --from-file=./secrets/yy
  - 通过指定generatorOptions.disableNameSuffixHash=true并将该kustomization.yaml作为base，将使得生成的configmap中不包含hash后缀。但这样就不会有滚动升级来实时更新configmap

- kustomize build

- gitops

- kyaml

- --load_restrictor=none
  - kustomize build -h
    - if set to 'LoadRestrictionsNone', local kustomizations may load files from outside their root. This does, however, break the relocatability of the kustomization. (default "LoadRestrictionsRootOnly")

- --enable_kyaml=false
  - x

- `standby promoted to primary`

- replication lag
  - It’s All About Replication Lag in PostgreSQL
    - https://www.percona.com/blog/replication-lag-in-postgresql/


```
$ kubectl apply -f runtime/local/overlay/osm/kustomization.yaml 
error: resource mapping not found for name: "" namespace: "" from "runtime/local/overlay/osm/kustomization.yaml": no matches for kind "Kustomization" in version "kustomize.config.k8s.io/v1beta1"
ensure CRDs are installed first


```

- type: Opaque
  - Opaque：不透明的
  - 使用base64编码存储信息


- Back-off pulling image
  - 意味着无法拉取所需的容器镜像

- kuboard
  - https://kuboard.cn/learning/
    - https://demo.kuboard.cn/kubernetes/kuboard-demo/namespace/default
