- docker-compose.yml 文件

- Installation
    - Rasp ubuntu
        - 

- 根据不同OS，安装不同的docker image

```
root@iZ11t8uvzvjZ:~/yapi# docker-compose up -d
ERROR: Network back-net declared as external, but could not be found. Please create the network manually using `docker network create back-net` and try again.

- network的作用是什么？
    - network_mode
        Docker中的host模式指定是容器与主机享受相同的network namespace，在这种情况下，我们访问主机端口就能访问我们的容器。比如说我们运行tomcat容器并且用-- network=host 来指定我们的网络模式为host，这样我们访问本机的8080端口就能访问到我们的tomcat容器。

        我曾经使用network_mode: host后一直在我的pc上访问不到容器的端口，telnet也不通，遇到这样的小伙伴，打好镜像别用mac测试就行了，我就被mac坑哭了。
        原文链接：https://blog.csdn.net/qq_20473985/article/details/104100176
```

curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
    gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor

echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/7.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-7.0.list


echo "mongodb-org hold" | dpkg --set-selections
echo "mongodb-org-database hold" | dpkg --set-selections
echo "mongodb-org-server hold" | dpkg --set-selections
echo "mongodb-mongosh hold" | dpkg --set-selections
echo "mongodb-org-mongos hold" | dpkg --set-selections
echo "mongodb-org-tools hold" | dpkg --set-selections

- 

- docker-compose services

- 在阿里云上启动的服务如何被外部访问，即 0.0.0.0 访问
