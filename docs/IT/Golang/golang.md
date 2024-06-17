比较适合什么领域？
https://www.zhihu.com/question/57404512

TinyGo on Arduino
https://blog.arduino.cc/2019/08/23/tinygo-on-arduino/

Go 包管理工具 dep 和 go module 的对比, 已经go vendor
https://liqiang.io/post/golang-package-manager-compare-module-vs-dep-d1b2db90
    - 从 dep 迁移到了 go module
    - vendor
    ```
    故事：失宠的 Vendor 目录
    Vendor目录是Golang从1.5版本开始引入的，为项目开发提供了一种离线保存第三方依赖包的方法。但是到了Golang 1.11之后，由于引入了Module功能，在运行go build时，优先引用的是Module依赖包的逻辑，所以Vendor目录就被“无视”了，进而可能发生编译错误， moudle 说还是很想他，于是 提供了 go mod vendor 命令用来生成 vendor 目录。这样能避免一些编译问题，依赖可以先从 vendor 目录进行扫描。
    ```
- 启动一个golang docker环境
```shell
docker pull golang
docker run -it golang /bin/sh
```

- go build
    - 将 .go 文件build成可执行文件
    
- GOPATH vs GOROOT vs GOBIN
    - GOROOT 表示 Go 的安装根目录，也就是 Go 的安装路径
    - GOPATH
        - 我们开发 Golang 项目时，需要依赖一些别的代码包，这些包的存放路径就与 GOPATH 有关。
        ```
        GOPATH="/home/vincent-zhong/go"
        $ ls /home/vincent-zhong/go
        pkg  src

        其中pkg目录为空

        其中src目录
        $ ls /home/vincent-zhong/go/src
        github.com  golang.org
            - 如果需要将整个源码添加到版本管理工具（Version Control System，VCS）中时，只需要添加 $GOPATH/src 目录的源码即可。bin 和 pkg 目录的内容都可以由 src 目录生成。
        ```
    - GOROOT 表示 Go 的安装根目录，也就是 Go 的安装路径
    ```
    GOROOT="/usr/lib/go-1.10"

    $ ls /usr/lib/go-1.10
    bin  pkg  src  test  VERSION

    其中 pkg 目录
    $ ls /usr/lib/go-1.10/pkg/
    include      linux_amd64_dynlink  linux_amd64_testcshared_shared  tool
    linux_amd64  linux_amd64_shared   obj

    其中 src 目录
    $ ls /usr/lib/go-1.10/src
    all.bash          compress   html           nacltest.bash  strconv
    all.bat           container  image          net            strings
    androidtest.bash  context    index          os             sync
    archive           crypto     internal       path           syscall
    bootstrap.bash    database   io             plugin         testing
    bufio             debug      iostest.bash   race.bash      text
    buildall.bash     encoding   log            race.bat       time
    builtin           errors     make.bash      reflect        unicode
    bytes             expvar     make.bat       regexp         unsafe
    clean.bash        flag       Make.dist      run.bash       vendor
    clean.bat         fmt        math           run.bat
    cmd               go         mime           runtime
    cmp.bash          hash       naclmake.bash  sort
    ```
    - `然后将可执行文件安装在$GOBIN的位置`

- go.mod
    - 使用go mod
        - 首先，必须升级go到1.11,目前版本是1.14
    - `go mod download` VS `go get`
        - What is the difference between go get command and go mod download command
            - https://stackoverflow.com/questions/66356034/what-is-the-difference-between-go-get-command-and-go-mod-download-command
        - x        

- 升级go版本
    - ubuntu下安装指定版本, e.g go1.20.2
```
wget  https://go.dev/dl/go1.20.2.linux-amd64.tar.gz
tar -xvf go1.20.2.linux-amd64.tar.gz 
mv go /usr/local
export GOROOT=/usr/local/go 
export PATH=$GOROOT/bin:$PATH
go version 
```

- GO111MODULE
```
GO111MODULE 有三个值：off, on和auto（默认值）。

GO111MODULE=off，go命令行将不会支持module功能，寻找依赖包的方式将会沿用旧版本那种通过vendor目录或者GOPATH模式来查找。
GO111MODULE=on，go命令行会使用modules，而一点也不会去GOPATH目录下查找。

```

- GOPROXY



```
error obtaining VCS status: exit status 128

- 原因：是因为我们的go版本太高了！因为之前安装的go版本是1.18的，是最新版，我们将go的版本降至1.16之后，再执行就可以成功了！
    - 原因可能是对的，但我不想这样解决，治标不治本

- go env -w GOFLAGS="-buildvcs=false"
    - OK,可以
```

- go mod tidy


```
$ ./go get github.com/gin-gonic/gin
go: go.mod file not found in current directory or any parent directory.
        'go get' is no longer supported outside a module.
        To build and install a command, use 'go install' with a version,
        like 'go install example.com/cmd@latest'
        For more information, see https://golang.org/doc/go-get-install-deprecation
        or run 'go help get' or 'go help install'.

solution:
$ go env -w GO111MODULE=off
```

```
bash: ./go: No such file or directory

选择64bit的tar
```

```
$ ./go get github.com/gin-gonic/gin
go: missing Git command. See https://golang.org/s/gogetcmd
package github.com/gin-gonic/gin: exec: "git": executable file not found in $PATH

# ./go get sigs.k8s.io/yaml
go: missing Git command. See https://golang.org/s/gogetcmd
package sigs.k8s.io/yaml: exec: "git": executable file not found in $PATH

都是用git去下载吗？
```

```
go: can only use path@version syntax with 'go get' and 'go install' in module-aware mode


```

```
# ./go get -d k8s.io/cli-runtime@3141d5468ff0d7b0af2c2991c64d1816d33e7721
package k8s.io/cli-runtime@3141d5468ff0d7b0af2c2991c64d1816d33e7721: cannot download, $GOPATH must not be set to $GOROOT. For more details see: 'go help gopath'


```

- go get 会 install 吗？ 还是只是download package ？
    - `go get -d` library, which only downloads it;
    - go get // verify if packages need to be downloaded, download if needed then compile
    - go get does two main things in this order:
    downloads and saves in $GOPATH/src/<import-path> the packages (source code) named in the import paths, `along with their dependencies`, then

    executes a go install

    The -d flag (go get -d) instructs go get to stop after downloading the packages; that is, it instructs go get not to do go install


小马技术 --【Go语言】包(模块项目)管理工具 - go mod, golang Modules
https://www.youtube.com/watch?v=cfcT_3ad-_0


- go dep  & go module
```
In my previous article, I used go-dep as my dependency management tool for a Go project. However, Go Modules have recently been released and announced as the official Go dependency management tool. A lot of Go 3rd libraries are being migrated to use Go Modules and require dependent projects to use Go Modules as well. Therefore, Go Dep is going to be deprecated soon.
```
