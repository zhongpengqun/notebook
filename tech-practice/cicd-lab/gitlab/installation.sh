# 注意！！！
# 对机器的硬件要求，内存至少4G，4G也不一定成功，8G可以，cpu最好2核吧（我的阿里云是2核），1核应该也行 


#1:拉取gitlab镜像
docker pull gitlab/gitlab-ce  
#2:生成挂载目录
mkdir -p /home/gitlab/etc/gitlab	
mkdir -p /home/gitlab/var/log
mkdir -p /home/gitlab/var/opt
#3:启动容器（用的时候调整下命令，为了便于查看，有换行符）

# docker run 
# -d                #后台运行，全称：detach
# -p 8443:443      #将容器内部端口向外映射
# -p 8090:80       #将容器内80端口映射至宿主机8090端口，这是访问gitlab的端口
# -p 8022:22       #将容器内22端口映射至宿主机8022端口，这是访问ssh的端口
# --restart always #容器自启动
# --name gitlab    #设置容器名称为gitlab
# -v /usr/local/gitlab/etc:/etc/gitlab    #将容器/etc/gitlab目录挂载到宿主机/usr/local/gitlab/etc目录下，若宿主机内此目录不存在将会自动创建
# -v /usr/local/gitlab/log:/var/log/gitlab    #与上面一样
# -v /usr/local/gitlab/data:/var/opt/gitlab   #与上面一样
# --privileged=true         #让容器获取宿主机root权限
# twang2218/gitlab-ce-zh    #镜像的名称，这里也可以写镜像ID

# -d：后台运行
# -p：将容器内部端口向外映射
# --name：命名容器名称
# -v：将容器内数据文件夹或者日志、配置等文件夹挂载到宿主机指定目录

Chinese language edition: docker run -d -p 8443:443 -p 8090:80 -p 8022:22 --restart always --name gitlab -v /usr/local/gitlab/etc:/etc/gitlab -v /usr/local/gitlab/log:/var/log/gitlab -v /usr/local/gitlab/data:/var/opt/gitlab --privileged=true twang2218/gitlab-ce-zh
Chinese language edition: docker run -d -p 8443:443 -p 8090:80 -p 8022:22 --restart always --name gitlab -v /usr/local/gitlab/etc:/etc/gitlab -v /usr/local/gitlab/log:/var/log/gitlab -v /usr/local/gitlab/data:/var/opt/gitlab --privileged=true gitlab/gitlab-ce:latest
# root  12345678


English language edition: // takes about 3 minutes to start finish
docker run -d -h gitlab -p 443:443 -p 8090:80  -p 8022:22  --name gitlab  --restart  always   -v /root/data/gitlab/config:/etc/gitlab  -v /root/data/gitlab/logs:/var/log/gitlab -v  /root/data/gitlab/data:/var/opt/gitlab  gitlab/gitlab-ce
# root pwd in /etc/gitlab/initial_root_password

