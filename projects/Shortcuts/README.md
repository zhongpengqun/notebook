##### docker development environment setup
Run project by following below instructions
```shell
docker build -t shortcuts . 
#docker run  -p 4200:4200 --rm -it --entrypoint bash shortcuts
docker run  -p 4200:4200 --rm -it -v $PWD/src:/app/src --entrypoint bash shortcuts
```
In container
```shell
if not shortcuts exists:
    ng new shortcuts
else:
    cd shortcuts

ng build
ng serve
```
能否mount volumn到一个running的container中
    - mount 与 volume 的区别
    


