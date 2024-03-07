Questions


Prerequistis:
- os: 
```shell
# lsb_release
LSB Version:    core-11.1.0ubuntu4-noarch:security-11.1.0ubuntu4-noarch
```
- install docker
```
apt-get update
apt  install docker.io
# docker -v
Docker version 20.10.12, build 20.10.12-0ubuntu4
```
- install kubeadmin
- install minikube


- Gitlab has its' own CI/CD, so what's the adventage of concourse(CI) and Jenkins(CD) ?

- Jenkins
    - How to trigger jenkins build when push changes to gitlab ?
        - need to use gitlab webhook, how to set it ?
        reference: 
        [牛逼!!!! 配置GitLab Push 自动触发Jenkins构建] https://www.cnblogs.com/yinzhengjie/p/9613270.html
        [Jenkins - 配置 Git Credentials]  https://blog.csdn.net/yanyc0411/article/details/127933809

    - How to generate jenkins ssh public key, in jenkins docker container ?
    - Now jenkins pull repo successfully, but next how to execute makefile in repo ?
        - [resolved] ls it
        - Use pipeline ?
    - Error
    ```shell
    HTTP ERROR 403 No valid crumb was included in the request

    [ solution ]
    https://blog.csdn.net/qq_33909098/article/details/113242437
    https://www.cnblogs.com/FengGeBlog/p/14974212.html
    ```

Start a postgresql database.
```shell
docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres
```




jenkins vs concourseCI
https://www.eficode.com/blog/jenkins-concourse


----------
jenkins: http://123.56.14.106:8082/
gitlab: 123.56.14.106:8090
concourse: http://123.56.14.106:8081/