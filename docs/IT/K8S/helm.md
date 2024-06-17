### Helm
- history
	- Helm在2016年成为了Kubernetes 1.4发行版的一部分
- why helm
	- 部署services的时候一般会有许多yaml文件,比如services.yaml, ingress.yaml, deployment.yaml，尤其是stateful的services的时候，当程序变得复杂了，手动部署不切实际
	- 但是真正的好处在于它在简化CI/CD管道中所扮演的角色
	- Helm自动维护发行版所有版本的数据库。因此，只要在部署过程中出现问题，回滚到以前的版本仅需一个命令
- Install Helm
    - Helm在2016年成为了Kubernetes 1.4发行版的一部分,是否内置了，比如安装了minikube，有内置的helm命令？
- Charts & release & repo
  ```
  Release 是运行在 Kubernetes 集群中的 chart 的实例。一个 chart 通常可以在同一个集群中安装多次。每一次安装都会创建一个新的 release。以 MySQL chart为例，如果你想在你的集群中运行两个数据库，你可以安装该chart两次。每一个数据库都会拥有它自己的 release 和 release name。
  ```

- 在所有的Helm替代产品中，Kustomize最受欢迎
- https://artifacthub.io/
- repo
  ```shell
  # helm repo list
  NAME    URL                                                    
  splunk  https://splunk.github.io/splunk-connect-for-kubernetes/
  ```
- helm的deployment.yaml文件它本质上就是一个k8s上的deployment资源声明，只是变量被模板取代了


```shell
$ helm install my-splunk-connect -f values.yaml splunk/splunk-connect-for-kubernetes
Error: INSTALLATION FAILED: cannot re-use a name that is still in use

solution:
$ helm delete my-splunk-connect
release "my-splunk-connect" uninstalled
```

- helm3 hello world

- helm lint

- helm UI
	- https://github.com/vmware-tanzu/kubeapps/

```
# helm install kibana elastic/kibana -n dapr-monitoring

Error: INSTALLATION FAILED: failed pre-install: job failed: BackoffLimitExceeded

---------
How to check helm log ?


```

- namespace terminating ?
  - https://zhuanlan.zhihu.com/p/418035941

- 使用helm安装gitlab
	- https://www.bilibili.com/video/BV1uY4y1J7Sa/?spm_id_from=333.337.search-card.all.click
