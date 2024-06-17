## GCC
- Bilibili 小布老师gcc https://www.bilibili.com/video/BV1rJ411V7EV?p=4&vd_source=397a53882c67614973bf614e08b1047f
	- 系统头文件与目录
		- /usr/local/include/
		- /usr/include/
		- /usr/local/lib/
		- /usr/lib/
	- search path
		- `-I`
			- 有了`-I`,可以提供compatible, #include</tmp/myhead.h>可以写成#include<myhead.h>
		- `-L`
	- archiver: ar
		- `.a`文件(库文件)是 archive文件的缩写吧？即多个.o文件的打包
		- ar cr libhello.a func1.o func2.o
	- 看到了 https://www.bilibili.com/video/BV1rJ411V7EV?p=7&vd_source=f209dde1a1d76e06b060a034f36bb756 16分

- 4 stages of compiling a c program
  - pre-processing
    - 预处理阶段主要工作是删除程序中所有的注释、处理以# 开头的命令，如：头文件的展开、宏定义的替换
	- 头文件的作用
		- 头文件就是像 #include<stdio.h> 这样的以 .h结束的文件
    - `gcc -E hello.c -o hello.i` 
  - Compiling
    - process `.i` into assembly language file
    - `gcc -S hello.i -o hello.s`
  - Assembling
    - process assembly language file to object file(binary file)
    - `gcc -c hello.s -o hello.o`
  - Linking
    - 汇编阶段将代码编译成了二进制文件，还需要和系统其他组件（比如标准库、动态链接库等）结合起来才能正常运行，比如调用print函数打印，在预处理阶段也只是将“stdio.h”头文件中的申明引入进来，没有函数的实现，那怎么调用它的呢？这就是链接的工作了，链接之前的操作都是对一个文件进行处理，而链接可以看作是对多个文件进行“打包”的过程，它将所有的目标文件以及系统组件组合成一个可执行文件。
    - `gcc hello.o -o hello`
  - What is `a.out` ? Which stage does it stuatide at ?

- key options
  - For `CFLAGS`
    - `-l`, `-L`
      ```shell
      gcc -l links with a library file.
      gcc -L looks in directory for library files.
      ```
    - `-O`
    - `-fPIC`
    - `-D
  - For `LDFLAGS`
    - `-lxxx`
    - `-Ldir`
    - `-WL, option`
    - `-static`
    - `-s`
  - `LIBS`

- https://www.bilibili.com/video/BV1RV411v75E/?spm_id_from=333.337.search-card.all.click
below are my notes of this video tutorial.

- Configure
  - CPPFLAGS
  - LDFLAGS

- 链接器 ld
- ldd
```shell
$ ldd /tmp/git/libexec/git-core/git-remote-https
 linux-vdso.so.1 (0x00007fff99f66000)
 libcurl.so.4 => not found
 libexpat.so.1 => not found
 libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f50b1a32000)
 libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f50b1813000)
 librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f50b160b000)
 libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f50b121a000)
 /lib64/ld-linux-x86-64.so.2 (0x00007f50b1c4f000)
```
  - You can run the `ldd --version` command to check your GLIBC version.

- ldconfig

- https://www.cnblogs.com/god-of-death/p/12767113.html

### note

```
    In file included from src/kerberos.c:19:0:
    src/kerberosbasic.h:17:10: fatal error: gssapi/gssapi.h: No such file or directory
     #include <gssapi/gssapi.h>
              ^~~~~~~~~~~~~~~~~
    compilation terminated.
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

google搜索：   src/kerberosbasic.h:17:10: fatal error: gssapi/gssapi.h: No such file or directory
```

GCC编译选项CFLAGS参数
https://www.cnblogs.com/god-of-death/p/12767113.html

linux编译参数CPPFLAGS、CFLAGS、LDFLAGS参数的理解
https://blog.csdn.net/lailaiquququ11/article/details/126691913



## GCC
- Bilibili 小布老师gcc https://www.bilibili.com/video/BV1rJ411V7EV?p=4&vd_source=397a53882c67614973bf614e08b1047f
- 4 stages of 

- key options
  - For `CFLAGS`
    - `-l`, `-L`
      ```shell
      gcc -l links with a library file.
      gcc -L looks in directory for library files.
      ```
    - `-O`
    - `-fPIC`
    - `-D
  - For `LDFLAGS`
    - `-lxxx`
    - `-Ldir`
    - `-WL, option`
    - `-static`
    - `-s`
  - `LIBS`

- https://www.bilibili.com/video/BV1RV411v75E/?spm_id_from=333.337.search-card.all.click
below are my notes of this video tutorial.

- Configure
  - CPPFLAGS
  - LDFLAGS

- ldd
- ldconfig

- https://www.cnblogs.com/god-of-death/p/12767113.html
