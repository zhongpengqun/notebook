# 官方文档
https://apscheduler.readthedocs.io/en/latest/userguide.html


- APScheduler has four kinds of components:
    - triggers
        - date: use when you want to run the job just once at a certain point of time
        - interval: use when you want to run the job at fixed intervals of time
        - cron: use when you want to run the job periodically at certain time(s) of day
        - 也能组合，apscheduler.triggers.combining
    - job stores
        - The default job store simply keeps the jobs in memory
        - Job stores must never be shared between schedulers.
    - executors
        - the choice of executors is usually made for you if you use one of the frameworks above. Otherwise, the default ThreadPoolExecutor should be good enough for most purposes.
        - If your workload involves CPU intensive operations, you should consider using ProcessPoolExecutor instead to make use of multiple CPU cores.
    - schedulers
        - Schedulers are what bind the rest together.You typically have only one scheduler running in your application.
        - The application developer doesn’t normally deal with the job stores, executors or triggers directly. Instead, the scheduler provides the proper interface to handle all those. 

BlockingScheduler: use when the scheduler is the only thing running in your process
BackgroundScheduler: use when you’re not using any of the frameworks below, and want the scheduler to run in the background inside your application
AsyncIOScheduler: use if your application uses the asyncio module
GeventScheduler: use if your application uses gevent
TornadoScheduler: use if you’re building a Tornado application
TwistedScheduler: use if you’re building a Twisted application
QtScheduler: use if you’re building a Qt application

```
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
# Initialize the rest of the application here, or before the scheduler initialization
------------------------
# This will get you a BackgroundScheduler with a MemoryJobStore named “default” and a ThreadPoolExecutor named “default” with a default maximum thread count of 10.
```

- By default, only one instance of each job is allowed to be run at the same time.
    - 因此默认情况下，只有一个job在运行

# 我的问题
- 有没有UI看job的执行情况，比如成功与否 ？
- an SQLAlchemyJobStore named “default” (using SQLite) 如何设置？