https://hub.docker.com/ 无法访问，docker pull不了了

- 这种情况下，如何pull到本地？
    - https://github.com/cmliu/CF-Workers-docker.io
        - http://docker.fxxk.dedyn.io

- 阿里云容器镜像服务
    - https://cr.console.aliyun.com/cn-hangzhou/instances
        - push image上去
            - https://cr.console.aliyun.com/repository/cn-hangzhou/zhongpengqun/wanderer/details

```
$ docker login --username=ZhongPengQun registry.cn-hangzhou.aliyuncs.com
Password: X*7
WARNING! Your password will be stored unencrypted in /home/ubuntu/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```



```
​官方的Docker hub是一个用于管理公共镜像的好地方，我们可以在上面找到我们想要的镜像，也可以把我们自己的镜像推送上去。但是，有时候我们的服务器无法访问互联网，或者你不希望将自己的镜像放到公网当中，那么你就需要Docker Registry，它可以用来存储和管理自己的镜像
```


- 搭建docker私有仓库


# 参考
https://developer.aliyun.com/article/869443?spm=5176.26934562.main.6.398745a7rANGmm

