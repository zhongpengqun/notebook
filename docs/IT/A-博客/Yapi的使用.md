# 我的环境
```
# lsb_release -a
LSB Version:    core-9.20170808ubuntu1-noarch:security-9.20170808ubuntu1-noarch
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.5 LTS
Release:        18.04
Codename:       bionic
```
```
# lscpu
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              1
On-line CPU(s) list: 0
Thread(s) per core:  1
Core(s) per socket:  1
Socket(s):           1
NUMA node(s):        1
Vendor ID:           GenuineIntel
CPU family:          6
Model:               85
Model name:          Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz
Stepping:            4
CPU MHz:             2500.008
BogoMIPS:            5000.01
Hypervisor vendor:   KVM
Virtualization type: full
L1d cache:           32K
L1i cache:           32K
L2 cache:            1024K
L3 cache:            33792K
NUMA node0 CPU(s):   0
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single pti ibrs ibpb stibp fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm mpx avx512f avx512dq rdseed adx smap avx512cd avx512bw avx512vl xsaveopt xsavec xgetbv1 arat
```

# 本地部署Yapi
### 安装mongodb
<a href="https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/"> 参考文章 </a>

(1)创建mongoDB容器数据卷目录
```
mkdir /data/mongo -p
```
(2)创建一个用于yapi的网络插件
```
docker network create yapi
```
(3)拉取MongoDB镜像, 用版本 mongo:4.2.21
```
docker pull registry.cn-hangzhou.aliyuncs.com/zhongpengqun/wanderer:mongo-4.2.21
```
(4)启动MongoDB容器
```
docker run -d \
  --name mongodb \
  --restart always \
  --net=yapi \
  -p 2717:27017 \
  -v /data/mongo:/data/db \
  -e MONGO_INITDB_DATABASE=yapi \
  -e MONGO_INITDB_ROOT_USERNAME=yapipro \
  -e MONGO_INITDB_ROOT_PASSWORD=yapi2023 \
  registry.cn-hangzhou.aliyuncs.com/zhongpengqun/wanderer:mongo-4.2.21
```
(5)进入mongo容器
```
docker exec -it mongodb /bin/bash
```
(6)进入mongo客户端
```
mongo localhost:27017
```
(7)初始化数据库,依次执行下面的命令
```
进入数据库
use admin;
创建用户名和密码
db.auth("yapipro", "yapi2023");
```
(8)创建yapi数据库
```
use yapi;
```
(9)创建给yapi使用的账号和密码，授予可操作的权限
```
db.createUser({
  user: 'zhongpengqun',
  pwd: 'zhongpengqun666',
  roles: [
 { role: "dbAdmin", db: "yapi" },
 { role: "readWrite", db: "yapi" }
  ]
});
```
(10)退出mongo客户端
```
exit
```
(11)退出mongo容器
```
exit
```

### docker启动Yapi
<a href="https://blog.csdn.net/Chimengmeng/article/details/132074922"> 参考文章 </a>

- 创建config.json文件
```
vim /data/yapi/config.json

{
   "port": "3000",
   "adminAccount": "yapiadmin@163.com",
   "timeout":120000,
   "db": {
     "servername": "mongo",
     "DATABASE": "yapi",
     "port": 27017,
     "user": "zhongpengqun",
     "pass": "zhongpengqun666",
     "authSource": ""
   },
   "mail": {
     "enable": true,
     "host": "smtp.163.com",
     "port": 465,
     "from": "*",
     "auth": {
       "user": "yapiadmin@163.com",
       "pass": "yapiadminpassword"
     }
   }
 }
```
然后初始化数据库
```
docker run -d --rm \
  --name yapi-init \
  --link mongodb:mongo \
  --net=yapi \
  -v /data/yapi/config.json:/yapi/config.json \
   registry.cn-hangzhou.aliyuncs.com/zhongpengqun/wanderer:yapi-1.9.5 \
  server/install.js
```


- 启动yapi容器, 用这个版本的Yapi: 1.9.5
```shell
docker run -d \
   --name yapi3 \
   --link mongodb:mongo \
   --restart always \
   --net=yapi \
   -p 3000:3000 \
   -v /data/yapi/config.json:/yapi/config.json \
   registry.cn-hangzhou.aliyuncs.com/zhongpengqun/wanderer:yapi-1.9.5 \
   server/app.js
```
查看log, 成功无报错
```
# docker logs -f bf375f3df1b89e5535c7a97509b30f5a1ba5092fc43d909ac0eb4e1a3c4eb58d
log: -------------------------------------swaggerSyncUtils constructor-----------------------------------------------
log: 服务已启动，请打开下面链接访问: 
http://127.0.0.1:3000/
log: mongodb load success...
```

成功后访问 http://localhost:3000 即可，初始化管理员账号在上面的 config.json 配置中 adminAccount的值，初始密码是 yapi.pro，可以登录后进入个人中心修改。



# 后记
之前我没用指定的yapi版本安装，出现了一些错误，解决方法记录如下
### 1.
```
bash: gpg: command not found
```
解决方法：
```shell
apt-get install gpg

// amd64 是你的cpu架构，我的因为是树莓派，所以是arm64
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/7.0 multiverse" uj /etc/apt/sources.list.d/mongodb-org-7.0.list

echo "mongodb-org hold" | dpkg --set-selections
echo "mongodb-org-database hold" | dpkg --set-selections
echo "mongodb-org-server hold" | dpkg --set-selections
echo "mongodb-mongosh hold" | dpkg --set-selections
echo "mongodb-org-mongos hold" | dpkg --set-selections
echo "mongodb-org-tools hold" | dpkg --set-selections
```


### 2.
```
Error: getaddrinfo ENOTFOUND yapi.demo.qunar.com
```
解决方法：
<a href="https://github.com/YMFE/yapi/issues/2180#issuecomment-1423701471"> Github issues </a>


### 3.
```
验证结果
执行脚本:
assert.notEqual(status, 404)
assert.deepEqual(body, {"code": 0})
Error: EROFS: read-only file system, mkdir '/sys/fs/cgroup/cpu/safeify'
Error: EROFS: read-only file system, mkdir '/sys/fs/cgroup/cpu/safeify'
```
解决方法：
<a href="https://blog.csdn.net/iaiti/article/details/125385365"> 参考文章 </a>

备份 sandbox.js
const Safeify = require('safeify').default;

module.exports = async function sandboxFn(context, script)
    // ...... safeify ......
    const safeVm = new Safeify({
        timeout: 3000,
        // zhong
        unrestricted: true,
        asyncTimeout: 60000
    })

    // ..................
    const result = await safeVm.run(script, context)

    // ............
    safeVm.destroy()
    return result
}
