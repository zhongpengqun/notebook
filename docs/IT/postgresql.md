### PostgreSQL

```
docker run -it --name postgres --restart always -e POSTGRES_PASSWORD='abc123' -e ALLOW_IP_RANGE=0.0.0.0/0 -v /home/postgres/data:/var/lib/postgresql -p 55433:5432 -d osstp-docker-local.artifactory.eng.vmware.com/mirrors/dockerhub/postgres:9.6
```

- Restore db from folder pgdata

- Tablespace

- ENGINE=InnoDB 什么意思 ？
    - InnoDB
        - 目前InnoDB採用雙軌制授權，一是GPL授權，另一是專有軟體授權。
        ```
        最开始用MySQL Administrator建数据库的时候，表缺省是InnoDB类型，也就没有在意。后来用Access2MySQL导数据的时候发现只能导成 MyISAM类型的表
        区别如下原来是MyISAM类型不支持事务处理等高级处理，而InnoDB类型支持。
        MyISAM类型的表强调的是性能，其执行数度比InnoDB类型更快，但是不提供事务支持，而InnoDB提供事务支持已经外部键等高级数据库功能。
        ```
        
