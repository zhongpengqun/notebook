- db.create_all() 没创建表
    - 须导入 from models import week



# apscheduler

```
Execution of job "job (trigger: interval[0:02:00], next run at: 2024-07-03 00:58:14 CST)" skipped: maximum number of running instances reached (1)


```

- 为什么需要使用flask-sqlalchemy？




```
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/orm/relationships.py", line 2157, in do_init
    self._generate_backref()
  File "/usr/local/lib/python3.9/site-packages/sqlalchemy/orm/relationships.py", line 2437, in _generate_backref
    raise sa_exc.ArgumentError(
sqlalchemy.exc.ArgumentError: Error creating backref 'farm' on relationship 'Farm.sections': property of that name exists on mapper 'mapped class Section->section'


```

- flask捕获model的字段update事件
    - on_model_change
