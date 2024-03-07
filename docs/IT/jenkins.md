## Jenkins
    - Installation
    - xx
    - How config github and gitlab project integration ?
    - Project types
    - Freestyle Project
        Apply to projects which is simple
    - Pipeline Project
        Apply to projects which more complex, e.g. includes test process, build process    
    - Jenkins manages github repo ?
        
    - properties
    - withCredentials
    - plugin: timestamps
    - What doese concept 'upstream' exactly mean in jenkins pipeline, and downstream ?

    - Multibranch Pipeline
        - 什么样的场景下非这种类型的pipeline不可呢？

- FreeStyle vs pipeline
    - Which senarior to use pipeline ?

- Tutorials
    - Complete Jenkins Pipeline Tutorial | Jenkinsfile explained
      https://www.youtube.com/watch?v=7KCS70sCoK0
    - Complete Jenkins Tutorial | Learn Jenkins From Scratch In 3 Hours 🎯| LambdaTest
      https://www.youtube.com/watch?v=nCKxl7Q_20I&t=8610s


- what's jenkins `build agent` ?
    - it's Equivalent to jenkins `slave` node ?
        - my understanding: yes

    - remote agent

- jenkins on cloud

- post-commit hook

- remote machine as jenkins node

- Build Triggers
    - Trigger builds remotely

- jenkins master and slave ?
    - Why need master and slave ?
        - officical doc: https://wiki.jenkins.io/display/JENKINS/Distributed+builds
        - https://blog.csdn.net/ruangong1203/article/details/78687450
        - jenkins支持主从模式，这将会把构建任务分发到多个从节点去执行，这样就可以支撑起多个项目的大量构建任务，同时，你可以提供多种环境（如：开发环境、生产环境）来对同一个项目进行测试和构建
            - 一个主机要作为jenkins的从节点需要满足两个条件：
                该主机需要装有java运行环境
                该主机允许jenkins master 服务器免密登录
    - if your Jenkins slave is docker container, how to add as a Node ?
        - https://www.youtube.com/watch?v=T2xoTC7gbbs

    - Tell Jenkins to run a specific project on a particular slave node
        - https://serverfault.com/questions/359793/tell-jenkins-to-run-a-specific-project-on-a-particular-slave-node
            - solution
            ```
            Set the "Restrict where this job can be run" check box in your job configuration and specify the name of your slave.

            If you add more slaves later, you can set labels for each slave and specify those in your job configs.
            ```
        - also can specific a node in pipeline
        ```
        pipeline {
            agent {label 'node1'}

            stages {
                stage('Hello') {
                    steps {
                        echo 'Hello World'
                    }
                }
            }
        }        
        ```
    - 如何从dashboard上看出一个node是master还是slave ？
    - todo, practice: 添加一个从节点


##### words appears in Jenkins dashboard
- Plugin `build blocker`
    - `Block build if certain jobs are running`

- `configure block level`
    - why need such configure ?
        - x
    - block on global level
        - x
    - block on node level
        - x

- `configure queue scanning`
    - x

- Docker plugin
    - `Restrict where this project can be run`
        - x

- Plugin: `build with parameter`
    - 

- `This project is parameterized`
    - x

- builtin varible `$gitlabBranch` vs `$gitlabSourceBranch`

- Is it possible to get gitlab repo tag in jenkins pipeline ?
    - Jenkins git-tag-message plugin ?
        - https://plugins.jenkins.io/git-tag-message/
        - how to install jenkins plugin ?
            - https://www.google.com.hk/search?q=jenkins+install+plugin+on+dashboard&newwindow=1&ei=pqcxZPD5MfigseMP1eW3sAY&oq=jenkins+install+plugin+on+dash&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgUIIRCgAToKCAAQRxDWBBCwAzoHCAAQigUQQzoGCAAQBxAeOgUIABCABDoECAAQHjoGCAAQCBAeSgQIQRgAUM0DWOokYJIwaAFwAXgAgAHfAYgB6BeSAQYwLjEyLjSYAQCgAQHIAQrAAQE&sclient=gws-wiz-serp#fpstate=ive&vld=cid:5f3e5d52,vid:EFLXlY_6Yq8


- Show jenkins build status and build result message to gitlab when jenkins build done.
    - x

- Jenkins plugin 制作, `.hpi` 文件

- executor

- create a project from copying an existing one.

- Bindings

- Pipeline Syntax


```
Also:   hudson.remoting.Channel$CallSiteStackTrace: Remote call to OSM-client-CI
		at hudson.remoting.Channel.attachCallSiteStackTrace(Channel.java:1743)
		at hudson.remoting.UserRequest$ExceptionResponse.retrieve(UserRequest.java:357)
		at hudson.remoting.Channel.call(Channel.java:957)
		at hudson.FilePath.act(FilePath.java:1070)
		at hudson.FilePath.act(FilePath.java:1059)
		at hudson.FilePath.mkdirs(FilePath.java:1244)
		at hudson.model.AbstractProject.checkout(AbstractProject.java:1202)
		at hudson.model.AbstractBuild$AbstractBuildExecution.defaultCheckout(AbstractBuild.java:574)
		at jenkins.scm.SCMCheckoutStrategy.checkout(SCMCheckoutStrategy.java:86)
		at hudson.model.AbstractBuild$AbstractBuildExecution.run(AbstractBuild.java:499)
		at hudson.model.Run.execute(Run.java:1818)
		at hudson.model.FreeStyleBuild.run(FreeStyleBuild.java:43)
		at hudson.model.ResourceController.execute(ResourceController.java:97)
		at hudson.model.Executor.run(Executor.java:429)
java.nio.file.AccessDeniedException: /home/worker
	at sun.nio.fs.UnixException.translateToIOException(UnixException.java:90)
	at sun.nio.fs.UnixException.rethrowAsIOException(UnixException.java:111)
	at sun.nio.fs.UnixException.rethrowAsIOException(UnixException.java:116)
	at sun.nio.fs.UnixFileSystemProvider.createDirectory(UnixFileSystemProvider.java:389)
	at java.nio.file.Files.createDirectory(Files.java:689)
	at java.nio.file.Files.createAndCheckIsDirectory(Files.java:796)
	at java.nio.file.Files.createDirectories(Files.java:782)
	at hudson.FilePath.mkdirs(FilePath.java:3237)
	at hudson.FilePath.access$1300(FilePath.java:212)
	at hudson.FilePath$Mkdirs.invoke(FilePath.java:1252)
	at hudson.FilePath$Mkdirs.invoke(FilePath.java:1248)
	at hudson.FilePath$FileCallableWrapper.call(FilePath.java:3050)
	at hudson.remoting.UserRequest.perform(UserRequest.java:212)
	at hudson.remoting.UserRequest.perform(UserRequest.java:54)
	at hudson.remoting.Request$2.run(Request.java:369)
	at hudson.remoting.InterceptingExecutorService$1.call(InterceptingExecutorService.java:72)
	at java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1128)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:628)
	at java.lang.Thread.run(Thread.java:834)
Finished: FAILURE
```


- Is it possible use env varibles when `jenkins custom message on success` ?

- Jenkins clear cache

- Gitlab create release时trigger jenkins job ？

- Trigger a jenkins build only when MR merged?


- Abort Jenkins build in shell script, is it possible ?
    - pipeline script is possible
    - curl -XPOST $BUILD_URL/stop
    - curl -XPOST $BUILD_URL_2/kill
        - 不起作用啊


- Accepted Merge Request Events 表示什么？
    - 表示当MR merge完成后触发
        - 如果job失败，是否会revert该MR ？
            - 不会，merge了就merge了，不会撤回了
    - 一个MR merge完成后，通过在MR下comment还能trigger jenkins job吗？
        - 还能trigger！


- `Inject environment variables to the build process` VS `This project is parameterised`
    - 

- returnStdout
    - 使用sh(script: 'cmd', returnStdout:true)将shell命令的结果返回输出，可以将返回的结果赋值给变量
- properties([
    