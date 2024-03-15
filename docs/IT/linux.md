###
- 标准输出和标准错误流
  - 标准输出流是流向标准输出设备（显示器）的数据。ostream类定义了三个输出流对象：cout，cerr，clog。
    - 来源：https://blog.csdn.net/qq_40456669/article/details/83690636
    - Linux中标准输出和标准错误的重导向： https://zhuanlan.zhihu.com/p/360549100


### bootloader
	- 大连理工大学 bootloader
		- https://www.bilibili.com/video/BV1bf4y1d7tp/?spm_id_from=333.788.recommend_more_video.-1
	- bootloader/uboot 简述
		- https://www.bilibili.com/video/BV1ta411b7nY/?spm_id_from=333.337.search-card.all.click
	- 固件
	- grub
		- gnu bootloader
		- todo, what's grub, https://www.bilibili.com/video/BV1wY41147he/?spm_id_from=333.337.search-card.all.click&vd_source=f209dde1a1d76e06b060a034f36bb756
	- uboot
	- 第11讲BootLoader的启动流程分析
		- https://www.bilibili.com/video/BV1cd4y1777h/?spm_id_from=333.788.recommend_more_video.-1&vd_source=f209dde1a1d76e06b060a034f36bb756
		- 内存初始化，硬件初始化
		- FLASH

推荐一本嵌入式工程师好书 mastering embedded linux programming
	- https://www.bilibili.com/video/BV1rP4y1A7qS/?spm_id_from=333.788.recommend_more_video.1&vd_source=f209dde1a1d76e06b060a034f36bb756
	- 嵌入式系统工程师技能要求介绍-Screen Recording 2022-01-30 at 11.21.38 AM
		- https://www.bilibili.com/video/BV12Y411t7Ww/?spm_id_from=333.999.0.0&vd_source=f209dde1a1d76e06b060a034f36bb756


### Linux
- Kernel Headers
https://unix.stackexchange.com/questions/47330/what-exactly-are-linux-kernel-headers
  - Install kernel headers https://linuxhint.com/install-kernel-headers-debian/
  - History: https://blog.csdn.net/trochiluses/article/details/9390855?spm=1001.2101.3001.6650.14&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-14-9390855-blog-54137564.pc_relevant_3mothn_strategy_and_data_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-14-9390855-blog-54137564.pc_relevant_3mothn_strategy_and_data_recovery&utm_relevant_index=14


### Shell
- bash VS zsh
- Is it possible to write a game by shell script ?
- $(1) means ?
- What does colon do in path ?
- eval
- chmod u+x
- make -p
- tar
  - `--strip-components`




```shell
curl --unix-socket /var/run/docker.sock http://localhost/version
```

```
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

## Shell
```Shell
tar zcvf dist.tar.gz -C dist 
```

```Shell
python3 -m ensurepip
```

Shell 中的 `:=` ?

make all

```shell
ldconfig
```

```
symbolic links & hard links
```


```shell
vzhong@vzhong-vm-2:~/osspi-cli$ sudo ln -s /home/vzhong/osspi-cli/build/resources/openssl/Openssl-3.0.5/lib64/libcrypto.so.3 /usr/lib/libcrypto.so.3
```

```shell
$ sudo ln -s /home/vzhong/osspi-cli/build/resources/openssl/Openssl-3.0.5/lib64/libssl.so.3 /usr/lib/libssl.so.3
```

```shell
openssl: error while loading shared libraries: libssl.so.3
```


```shell
/usr/bin/install -c /home/vzhong/glibc/glibc-2.36/build/elf/ld.so /lib64/ld-linux-x86-64.so.2.new
mv -f /lib64/ld-linux-x86-64.so.2.new /lib64/ld-linux-x86-64.so.2
rm -f /usr/bin/ld.so.new
Inconsistency detected by ld.so: dl-call-libc-early-init.c: 37: _dl_call_libc_early_init: Assertion `sym != NULL' failed!
Makefile:1390: recipe for target '/usr/bin/ld.so' failed
make[2]: *** [/usr/bin/ld.so] Error 127
make[2]: Leaving directory '/home/vzhong/glibc/glibc-2.36/elf'
Makefile:484: recipe for target 'elf/subdir_install' failed
make[1]: *** [elf/subdir_install] Error 2
make[1]: Leaving directory '/home/vzhong/glibc/glibc-2.36'
Makefile:12: recipe for target 'install' failed
make: *** [install] Error 2
```

```shell
Inconsistency detected by ld.so: dl-call-libc-early-init.c: 37: _dl_call_libc_early_init: Assertion `sym != NULL' failed!
```

- OS
  - Lock
  - linux cpio

- xrdb
- build-essential
- ttyd

- sudo sysctl fs.inotify.max_user_instances=8192
	```
	fs.inotify.max_user_watches：表示同一用户同时可以添加的watch数目（watch一般是针对目录，决定了同时同一用户可以监控的目录数量）
	```

### Alpine Linux

### busybox
- busybox包含的400多个常用命令，是哪400个？


- sticky bit set

- Drive, Partition, and Volumes in Linux
	- Differences
		- drive is commonly used to refer to an actual physical storage device. Examples of these devices are hard-disk drives and `solid-state` drives.
		- partitions are subdivisions of a single physical storage drive
			- It offers the flexibility to divide a large physical storage device into a few smaller independent storage units.
		- volume is a higher level of abstraction over the partition. Specifically, the volume helps us in managing our storage in the form of aggregated storage space, instead of the individual storage device
	- \#共同点#\ common ground
		- they are all `non-volatile` computer storage

- Shell有哪些数据类型?
	- 数组
		- 如何操作数组？获取某个item，获取整个数组length，获取所有items

- 各个标点符号在shell中的含义..
	- ()
	- (())
	- []
	- [[]]
	- {}	

- 单引号与双引号的区别
- linux shell file中cd到某个目录，然后当前路径变化，怎么弄？

- How to write POSIX compliant shell script ? To avoid bash-isms.

### man 命令的使用
- 如何快速查看某个flag的用法？
- `使用man命令查看etc下的文件不需要给出完整地路径，只需要给出文件名即可`
	- man password
	- man 5 password


### Shell
- bash VS zsh
- Is it possible to write a game by shell script ?
	- Yes, tetris by shell, https://github.com/liungkejin/Bash-Games/blob/master/tetris.sh
- $(1) means ?
- What does colon do in path ?
- eval
- chmod u+x
	-
- make -p
- tar
  - `--strip-components`
- declare
	- https://www.runoob.com/linux/linux-comm-declare.html


```shell
curl --unix-socket /var/run/docker.sock http://localhost/version
```

- whatis

```
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

- wget http://xx.com/x.zip 下载下来的文件不一定是你想要的x.zip文件，如果这里url是一个html页面，只是叫了 http://xx.com/x.zip 这个名字而已，那么你wget download下来虽然是zip文件，但是unzip后是html file

## Shell
```Shell
tar zcvf dist.tar.gz -C dist 
```

Shell 中的 `:=` ?

make all

shell中的段落注释

```shell
ldconfig
```

```
symbolic links & hard links
```


```shell
vzhong@vzhong-vm-2:~/osspi-cli$ sudo ln -s /home/vzhong/osspi-cli/build/resources/openssl/Openssl-3.0.5/lib64/libcrypto.so.3 /usr/lib/libcrypto.so.3
```

```shell
$ sudo ln -s /home/vzhong/osspi-cli/build/resources/openssl/Openssl-3.0.5/lib64/libssl.so.3 /usr/lib/libssl.so.3
```

- 软连接(symbolic link aka soft link)与硬链接(hard link)的区别
	- inode
		- A file in the file system is basically a link to an inode.
		- A hard link, then, just creates another file with a link to the same underlying inode.
	- just like shortcut in windows
	- softlink's inode number is different from origin file's inode number
		- shortcut will be invalid when origin file is deleted, as well as softlink
	- why soft link ?
	- Hard link
		- Different name of the same file
		- same inode number, same file size
		- just like a copy of origin file
		- if origin file is deleted, hard link still contains the data.
	- How to create a hard link ?
	```
	ln sfile1file link1file
	```

- /usr/bin/aws vs /usr/local/bin/aws

```shell
openssl: error while loading shared libraries: libssl.so.3
```


```shell
/usr/bin/install -c /home/vzhong/glibc/glibc-2.36/build/elf/ld.so /lib64/ld-linux-x86-64.so.2.new
mv -f /lib64/ld-linux-x86-64.so.2.new /lib64/ld-linux-x86-64.so.2
rm -f /usr/bin/ld.so.new
Inconsistency detected by ld.so: dl-call-libc-early-init.c: 37: _dl_call_libc_early_init: Assertion `sym != NULL' failed!
Makefile:1390: recipe for target '/usr/bin/ld.so' failed
make[2]: *** [/usr/bin/ld.so] Error 127
make[2]: Leaving directory '/home/vzhong/glibc/glibc-2.36/elf'
Makefile:484: recipe for target 'elf/subdir_install' failed
make[1]: *** [elf/subdir_install] Error 2
make[1]: Leaving directory '/home/vzhong/glibc/glibc-2.36'
Makefile:12: recipe for target 'install' failed
make: *** [install] Error 2
```

```shell
Inconsistency detected by ld.so: dl-call-libc-early-init.c: 37: _dl_call_libc_early_init: Assertion `sym != NULL' failed!
```

- OS
  - Lock
  - linux cpio

- xrdb
- build-essential

- tty
	- ttyd



### Alpine Linux

### busybox
- busybox包含的400多个常用命令，是哪400个？



- 各个不同type shell之间的语法区别

```
$ VERSION_DIFF=`git diff master..develop | VERSION.txt`
fatal: ..: '..' is outside repository
VERSION.txt: command not found
```

- grep

- function的参数怎么传？比如传个path /tmp/xx.sh 时



- set命令可以用来定制shell环境
	- set -e
		- 在shell脚本开头加上set -e，这句话告诉bash 如果任何语句的执行结果不是true，就直接退出shell脚本
	- set +e
		- set +e 表示关闭 -e选项，即使出错也依然向下执行脚本
	- set -x
	- set +x
	- set -o errexit
		- 使用选项“o”来打开或者关闭选项。例如打开选项：set -o 选项，关闭选项目：set +o 选项
		- errexit 当命令返回一个非零退出状态（失败）时退出
		```shell
		set +o errexit
		ls /no-such-path
		echo "+o is set!!"

		output:
		+o is set!!
		```


- echo $?
	- 取的上条命令的返回值


- 单引号 & 双引号
```shell
$ echo $mm1
master_python3

$ echo $mm2
develop

$ git branch | grep -vw "$mm1\|$mm2"
  develop_python3
  master
  topic/vzhong/PORSCHE-5409-Push-versioned-osstpclients-bundle-to-Artifactory
  topic/vzhong/PORSCHE-5770-Remove-confusing-log-output-from-the-osstp-load
  topic/vzhong/PORSCHE-5836-Confusing-output-in-osstp-load-Skipped-creation-of-129-requests
  vz-test
  vz-test-2
  vzhong-production-mock

$ git branch | grep -vw '$mm1\|$mm2'
  develop
  develop_python3
  master
* master_python3
  topic/vzhong/PORSCHE-5409-Push-versioned-osstpclients-bundle-to-Artifactory
  topic/vzhong/PORSCHE-5770-Remove-confusing-log-output-from-the-osstp-load
  topic/vzhong/PORSCHE-5836-Confusing-output-in-osstp-load-Skipped-creation-of-129-requests
  vz-test
  vz-test-2
  vzhong-production-mock
  ```


- To copy ownership of one file to another
	- chown --reference=greek1 greek2
		- changed ownership of 'greek2' from root:root to root:group1
		

- curl -X DELETE

- $ tar -zcf /tmp/ttest/ff.tar.gz /tmp/ttest/*
  tar: Removing leading `/' from member names
	- 去除文件名中前导的根目录“/”，tar 命令在压缩文件时，默认会取相对路径，不会取从根路径下来的绝对路径，所以，如果待压缩的源路径是绝对路径，便会报该错误

- .tar.bz2  VS .tar.gz
	- .tar.gz (or shorter .tgz)
	- bzip2是一个压缩能力更强的压缩程序，.bz2结尾的文件就是bzip2压缩的结果。与bzip2相对的解压程序是bunzip2。tar中使用-j这个参数来调用gzip。下面来举例说明一下：
	tar -cjf all.tar.bz2 *.jpg
	解压： tar -xjf all.tar.bz2


- lsof
	- lsof 没任何显示，或没有期望的显示，也有可能是没用sudo

- kill all processes from lsof
	- sudo lsof -i:9998 | awk 'FNR >= 2 {print $2}' |xargs sudo kill -9 $1

```
$ sudo lsof -i:9998 | awk '{print $2}'
PID
476530
476537

$ sudo lsof -i:9998 | awk 'FNR >= 2 {print $2}'
476530
476537
```

有没有这样的工具，比如我在一个shell文件里输入 cp -, 然后会有参数提示 ？

- sed
	- 提取 xx 和 yy 之间的字符
		- 

- $ curl -G -d 'g=publish' -d 'a=osstpclients3' https://microhard.com/api/test/latestVersion

```
 [[: not found

bash有[[, 但是sh没有该语法
```

- mount
	- 查看已经mount的目录
		- 要查看当前系统中的所有挂载点，可以直接在终端中输入 mount 命令
		- /etc/fstab
			- 一般也可以通过该命令来查看 mounted 的 filesystem
	- sudo mount -t nfs -o nolock x.si01.oc.xxx.com:/xxx /tmp/yyy
		- sudo umount /tmp/yyy
	- terminologies
		- partition
			- storage devices VS partitions
		- mount device
		- Mount point
			- the directory where the partition or disk will be mounted
			- Mounting means attaching a partition, hard disk, or file system to the system in use
			- Similarly, when we insert a CD in Windows operating systems, the default mount point would be D:/ or Cdrom, the “directory” where files become accessible to the user.Of course, this is different than in Linux because in Linux mount points are regular directories, like any other directory.
			- Usually, the mount point is a dedicated directory for mounting purposes, but users can use any directory as a mount point, including directories containing files and subdirectories
			- Normally, the default mount points in Linux are /media, /mnt, /usb and /media/mnt, but users can mount devices in any directory.

- jq
	- $ echo '{"foo": "bar"}' | jq -r '.foo'
		bar

- shell函数返回值赋值给变量

- local 关键字
- 如何在一个shell文件中把一个长的command拆解成多段，以方便阅读
	- 

How to Use the ts Command to Add Timestamps to Output
	- https://levelup.gitconnected.com/how-to-use-the-ts-command-to-add-timestamps-to-output-686c92ef6124#:~:text=The%20ts%20command%20is%20a,timestamps%20according%20to%20their%20needs.
		- standard streams (stdin, stdout, and stderr), pipes, and redirection in Linux
		- `sudo apt-get install moreutils`

- zip all files which has no extension

- shell set variable from function return value
	- https://stackoverflow.com/questions/12919486/assign-the-returned-value-of-a-function-to-a-variable-in-unix-shell-script
		- The value returned by the function is stored in $?
			- only can return integer

- How to Extract Tar Files to Specific or Different Directory in Linux
	- tar -xf file_name.tar.gz --directory /target/directory

- strip quotes
	- file_name=$(echo "$_file_name" | tr -d '"')

- /etc/apt/sources.list
```
type     软件包所在仓库的地址             发行版     软件包分类
deb http://site.example.com/debian distribution component1 component2 component3
deb-src http://site.example.com/debian distribution component1 component2 component3

e.g
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse

deb: 二进制
deb-src: 源代码
	- main，restricted，universe，multiverse有什么区别
		- 这是按软件的自由度来分的。
			main:完全的自由软件。
			restricted:不完全的自由软件。
			universe:ubuntu官方不提供支持与补丁，全靠社区支持。
			multiverse：非自由软件，完全不提供支持和补丁。
	- https://renenyffenegger.ch/notes/Linux/fhs/etc/apt/sources_list
	- /etc/apt/sources.list.d/*.list
```

- if [ ! -z $STRING ]; then
    - #如果$JAVA_EXEC的长度为零则为假

- which kustomize || exit 1

- pushd
	- 相比cd，不需要 cd ../../xx （不需要知道当前路径与目标路径的距离）

- https://stackoverflow.com/questions/67880900/curl-doesnt-return-anything

- 查看端口是否open
	- $ echo > /dev/tcp/192.168.1.7/12001 && echo "Port is open"
	- 打开一个端口


- source.list VS sources.list VS sources.listd


- arm64/ VS armhf/



ubuntu@ubuntu:~$ df -h
文件系统        容量  已用  可用 已用% 挂载点
...
/dev/sda1        58G  256K   58G    1% /media/ubuntu/KINGSTON



- systemctl daemon-reload
	- `命令并不会重新启动任何服务。它仅用于加载配置文件`

- sysctl user.max_user_namespaces=28633
	- `该参数限制用户所拥有的 namespace 数量。在 Kubernetes 中，每个容器都需要自己的 namespace，因此请确保将此值设置足够高以满足您的集群需求`

- 磁盘 & 分区

- tar -xvf drought-ET-irrigation-master.tar
