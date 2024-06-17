- testbed

https://locust.io/

- mock 是什么意思？


- 软件测试方法包括：
   - 白盒测试(White Box Testing)
   - 黑盒测试(Black Box Testing)
      - 功能性测试、容量测试、安全性测试、负载测试、恢复性测试、标杆测试、稳定性测试、可靠性测试等
         - 标杆测试, 比如一款新产品上线，都有用来对标的友商设备
   - 灰盒测试
   - 静态测试
   - 动态测试
   - 单元测试
      - 两个步骤：人工静态检查法与动态执行跟踪法

docker run -d \
   --name yapi33 \
   --link mongodb:mongo \
   --restart always \
   --net=yapi \
   -p 3000:3000 \
   -v /data/yapi/config.json:/yapi/config.json \
   zhongyapi:latest \
   server/app.js

### Software test

```shell
coverage run --branch --source=. --omit=*/tests*,*__init__* -m unittest discover
```

---------
https://www.bilibili.com/video/BV1LD4y1o79K/?spm_id_from=autoNext&vd_source=f209dde1a1d76e06b060a034f36bb756

https://www.gutenberg.org/files/1998/1998-h/1998-h.htm

https://www.gutenberg.org/files/1998/1998-h/1998-h.htm#link2H_INTR

2022年09月21日10:49:03

- test --> side effect

- How coverage test a specific case ?

```python
>>> try:
...     assert 1==2
... except Exception as exc:
...     print(str(exc))
...

>>>
```

### Test
- 回归测试
