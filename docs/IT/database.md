### PostgreSQL

```
docker run -it --name postgres --restart always -e POSTGRES_PASSWORD='abc123' -e ALLOW_IP_RANGE=0.0.0.0/0 -v /home/postgres/data:/var/lib/postgresql -p 55433:5432 -d osstp-docker-local.artifactory.eng.vmware.com/mirrors/dockerhub/postgres:9.6
```



## SQL
- select mt where 
    - Join
- SQL语句“create table <table_name> as select ...”用于创建普通表或临时表，并物化select的结果。某些应用程序使用这种结构来创建表的副本。一条语句完成所有工作，因此您无需创建表结构或使用其他语句来复制结构。
- select distinct
    - https://www.runoob.com/sql/sql-distinct.html
- select count(1)  &  select count(*)
    - 功能是一样的？返回rows的总数
- having count(1)>1
```
作用是保留包含多行的组。

SELECT
　　class.STUDENT_CODE
FROM
　　crm_class_schedule class
GROUP BY class.STUDENT_CODE
HAVING
　　count(*) > 1

执行结果是将[crm_class_schedule]表中[STUDENT_CODE]字段重复的数据显示出来。
```

## tool for viusalize db design


- pgadmin connect db container

- WAL file


- select * from user where name like '%vincent';
- select * from user where name like '*vincent';
    - 区别: https://blog.csdn.net/c_base_jin/article/details/74360242


## SQLite
- sqlite 中 varchar 的最大长度是多少 ？如果不指定长度，默认的是多少？
- 客户端软件
    - https://www.sqliteviewer.com/
    - https://dbeaver.io/


- data modeling tools
    - https://erd.dbdesigner.net/designer/schema/guest_template