#docker build - < nginx.Dockerfile
docker build -f nginx.Dockerfile -t nginx-demo-image .
docker run -it -p 9998:80 -v $PWD/demo.conf:/etc/nginx/conf.d/demo.conf nginx-demo-image:latest /bin/sh
