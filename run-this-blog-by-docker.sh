# /bin/sh

# todo, 有点问题，run不起来
# Docker run it, it is the best! refer to https://medium.com/@edsonalcalamx/running-nethereum-docs-with-docker-5b8a4c25d42f
# docker rmi -f blog
# docker rm -f $(docker ps |grep blog |awk '{ print $1 }')
# docker build -t blog .
# sudo kill -9 $(sudo lsof -i:7777 | awk 'NR>1' | awk '{print $2}')
# docker run -d -p 7777:7777 blog mkdocs serve -a 0.0.0.0:7777

# Then http://localhost:7777 will be able to access this blog

# 先把 7777 的端口程序kill掉
docker-compose down
docker-compose build
docker-compose up