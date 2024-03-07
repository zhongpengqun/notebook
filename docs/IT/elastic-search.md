#### elastic search
- how to deploy a distributed elasticsearch ?
- concepts
    - https://blog.csdn.net/bbj12345678/article/details/108418125
    - cluster
        - what's the benefits of cluster ?
        - node
        ```
        在测试的环境中，我可以把多个 node 运行在一个 server 上。在实际的部署中，大多数情况还是需要一个 server 上运行一个 node
        ```
        - ingest
        - document
            - coresponds to record in db
        - type
            - corresponds to table in db ?
        - index
            - corresponds to db ?
        - shard
            ```
            一个索引可以存储超出单个结点硬件限制的大量数据。比如，一个具有10亿文档的索引占据1TB的磁盘空间，而任一节点都没有这样大的磁盘空间；或者单个节点处理搜索请求，响应太慢。
            ```
            - what's the benefits ?





- elasticsearch & kibana
    - reference: https://levelup.gitconnected.com/docker-compose-made-easy-with-elasticsearch-and-kibana-4cb4110a80dd
        - docker-compose.yml

```
version: "3.0"
services:
    elasticsearch:
        container_name: es-container
        image: docker.elastic.co/elasticsearch/elasticsearch:7.11.0
        environment:
        - xpack.security.enabled=false
        - "discovery.type=single-node"
        networks:
        - es-net
        ports:
        - 9200:9200
    kibana:
        container_name: kb-container
        image: docker.elastic.co/kibana/kibana:7.11.0
        environment:
        - ELASTICSEARCH_HOSTS=http://es-container:9200
        networks:
        - es-net
        depends_on:
        - elasticsearch
        ports:
        - 5601:5601
networks:
    # 
    es-net:
        driver: bridge
```
then access http://localhost:5601 kabina homepage.


- helm install es & kibana, for net blocked in china.
    - helm kibana
        - https://www.cnblogs.com/hanshengli/p/14718342.html



```
$ kubectl get pods
NAME                     READY   STATUS             RESTARTS      AGE
elasticsearch-master-0   0/1     CrashLoopBackOff   4 (33s ago)   8m22s
elasticsearch-master-1   0/1     Running            0             8m22s
elasticsearch-master-2   0/1     CrashLoopBackOff   4 (21s ago)   8m21s





# kubectl get secrets --namespace=default elasticsearch-master-credentials -ojsonpath='{.data.password}' | base64 -d
# curl -k https://localhost:9200/_cluster/health -u elastic:u0pYkBYslItbI0W5

{"error":{"root_cause":[{"type":"master_not_discovered_exception","reason":null}],"type":"master_not_discovered_exception","reason":null},"status":503}


# curl -X GET -k 'https://localhost:9200/?pretty=true' -u elastic:u0pYkBYslItbI0W5
{
  "name" : "elasticsearch-master-1",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "_na_",
  "version" : {
    "number" : "8.5.1",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "c1310c45fc534583afe2c1c03046491efba2bba2",
    "build_date" : "2022-11-09T21:02:20.169855900Z",
    "build_snapshot" : false,
    "lucene_version" : "9.4.1",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
Indicates that it's ok, but
# curl -k https://localhost:9200/_cat/health -u elastic:u0pYkBYslItbI0W5
stucked
ps: all apis, https://gist.github.com/anselmo/ab18baebfdf459c38c017538a4daf49b


change as: clusterHealthCheckParams: "local=true"
↓
# kubectl get pods
NAME                     READY   STATUS             RESTARTS        AGE
elasticsearch-master-0   0/1     CrashLoopBackOff   5 (2m31s ago)   10m
elasticsearch-master-1   1/1     Running            0               10m
elasticsearch-master-2   0/1     CrashLoopBackOff   5 (2m31s ago)   10m

# curl -X GET -k 'https://localhost:9200/_cluster/health?pretty=true' -u elastic:9xDSmevMzvaloe0N
{
  "error" : {
    "root_cause" : [
      {
        "type" : "master_not_discovered_exception",
        "reason" : null
      }
    ],
    "type" : "master_not_discovered_exception",
    "reason" : null
  },
  "status" : 503
}
```



不是minikube的时候memory需要设置得大一点，否则elasticsearch不能跑起来
```
$ minikube start --nodes 2 --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 2 --kubernetes-version=v1.23.1 --memory=12000
```

