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