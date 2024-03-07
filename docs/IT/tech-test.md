- testbed

https://locust.io/

- mock 是什么意思？





docker run -d \
   --name yapi33 \
   --link mongodb:mongo \
   --restart always \
   --net=yapi \
   -p 3000:3000 \
   -v /data/yapi/config.json:/yapi/config.json \
   zhongyapi:latest \
   server/app.js