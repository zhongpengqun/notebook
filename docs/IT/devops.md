### 先运行一个container，该container运行着一个web server，当我们去curl它的api时候，stdout会有输出，可以用于测试fluentd

```
docker run -p 18080:80 --name nginx -d nginx:1.10
```

- Is it possible to use stdout/stderr as fluentd source?
    - https://stackoverflow.com/questions/54778074/is-it-possible-to-use-stdout-stderr-as-fluentd-source

- fluentd如何收集全部pod的log，假设pod的log在/var/log/x.log

### kerberos
- https://www.youtube.com/watch?v=5N242XcKAsM


- fluentd splunk
    - fluentd send k8s pods logs to splunk
        - 参考：https://cloud.tencent.com/developer/ask/sof/477135
    
    - TODO: 搭建日志系统之 Fluentd
        - https://www.bilibili.com/video/BV15y4y1m7Fe/?spm_id_from=333.337.search-card.all.click&vd_source=f209dde1a1d76e06b060a034f36bb756

- http://www.pangxieke.com/linux/docker-logging-fluentd.html
	- fluentd 是一个开源的数据收集器，它原生就支持 JSON 格式，因此你可以在主机上运行一个单独的 fluentd 实例并配置它来 tail `每个容器`的 JSON 文件
	- 我的理解：fluentd可以运行在host上，或作为一个container运行，2种方法都能收集containers的log
	- example of fluentd.conf
	```
	<source>
	@type forward
	</source>

	<match *>
	@type stdout
	</match>
	```


### fluentd
- vmware/kube-fluentd-operator
    - Installation
        - https://github.com/vmware/kube-fluentd-operator
    - Run
    ```shell
    helm install kfo ${CHART_URL} \
    --set rbac.create=true \
    --set image.tag=v1.16.8 \
    --set image.repository=vmware/kube-fluentd-operator
    ```
    - From the readme, why it needs to `build` ?
        - create fluentd image, then run it as daemonset container ?

    - `It compiles a Fluentd configuration from configmaps (one per namespace)`
	- 这样的话，如果我只想monitor一个ns，其他ns不想monitor怎么办？
    - `KFO also extends the Fluentd configuration language making it possible to refer to pods based on their labels and the container name pattern`
	- 是什么原理呢？
    - `Finally, it is possible to ingest logs from a file on the container filesystem. While this is not recommended, there are still legacy or misconfigured apps that insist on logging to the local filesystem.`
	- 是否monitor container的stdout才是该repo的主要目的?
    - `@type record_transformer`
    - container label

    - todos
	- forward logs to elasticsearch

- output plugins
- '当微服务的时候，多台host运行着各自的containers,如果需要查看全部的log，需要到3台host分别查看，但是如果用了fluentd就不一样了'


```shell
$ helm install kfo ${CHART_URL}   --set rbac.create=true   --set image.tag=v1.16.8   --set image.repository=vmware/kube-fluentd-operator  --set datasource=crd

$ kubectl logs -f kfo-log-router-5rw5l

2023-03-06 09:14:16 +0000 [warn]: #0 [in_systemd_docker] Systemd::JournalError: No such file or directory retrying in 1s
2023-03-06 09:14:17 +0000 [warn]: #0 [in_systemd_bootkube] Systemd::JournalError: No such file or directory retrying in 1s
2023-03-06 09:14:17 +0000 [warn]: #0 [in_systemd_kubelet] Systemd::JournalError: No such file or directory retrying in 1s
```


For locally investigation, you can register a fluentd cloud log. e.g https://www.loggly.com/
    - loggly
        - token: https://zhongpengqun.loggly.com/tokens


- 如何使用 fluentd plugin

- https://github.com/marcel-dempers/docker-development-youtube-series/blob/master/monitoring/logging/fluentd/introduction/readme.md

- @label
    - https://www.cnblogs.com/chuanzhang053/p/16888901.html

- @type tail
```
<parse>配置项需要通过@type参数来指定解析器的类型。Fluentd内核绑定了很多有用的解析器插件，也可以根据需要安装其他第三方解析器。
<parse>
  @type apache2
</parse>
这里，@type指定使用apache2这个解析器来解析输入日志。
```

- match标签




#### plan
- create a docker image that print 'hello world' continously.
- push this image to docker.io

- forwart to local elasticsearch ?
```
1. 
```

- forward to external elaticsearch ?

- Kubernetes安装EFK日志收集
    - https://blog.csdn.net/heian_99/article/details/123405383
        - not tried it yet
    - https://v1-0.docs.dapr.io/zh-hans/operations/monitoring/logging/fluentd/
        - looks like this is more kaopu

- Sidecar vs Agent

 - @type

- 工作中遇到的一个问题：fluentd只能forward log file到splunk，对吧？

```
$ kubectl apply -f f.yml
fluentdconfig.logs.vdp.vmware.com/fluentd-config created
```


- nginx `location`
```
    location /b/ {
        alias /srv/src/xx/;
    }
    location /a/ {
        alias /srv/src/;
    }

so how to access file /srv/src/xx/cc.tar from URL
/a/b/cc.tar   or  /b/cc.tar  ?
``` 
    - root VS alias
        - root 是拼接起来
        ```
            location /lxx {
                root /etc/nginx/conf.d;
            }

            http://10.79.128.26:9998/lxx/vz.txt
            open() "/etc/nginx/conf.d/lxx/vz.txt" failed (2: No such file or directory)
        ```
        - alias 则是替换
            - open() "/etc/nginx/conf.d/vz.txt" failed (2: No such file or directory

```
2023/07/23 08:01:29 [error] 785#785: *1 open() "/etc/nginx/html/l/vz.txt" failed (2: No such file or directory), client: 10.111.0.201, server: localhost, request: "GET /l/vz.txt HTTP/1.1", host: "10.79.128.26:9998"
```
    - NGINX Alias vs Root
        - 
