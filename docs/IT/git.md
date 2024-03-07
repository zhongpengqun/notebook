- git refs & tags
    - 经典: http://itmyhome.com/progit/eb04be8dd776142cd3fbb52e27694746/92abc307328bd414f4cd589a4400994b.html
        - 你可以执行像 git log 1a410e 这样的命令来查看完整的历史，但是这样你就要记得 1a410e 是你最后一次提交，这样才能在提交历史中找到这些对象。你需要一个文件来用一个简单的名字来记录这些 SHA-1 值，这样你就可以用这些指针而不是原来的 SHA-1 值去检索了。

        - 每当你执行 git branch (分支名称) 这样的命令，Git 基本上就是执行 update-ref 命令，把你现在所在分支中最后一次提交的 SHA-1 值，添加到你要创建的分支的引用。

        - tags
        Tag 对象非常像一个 commit 对象——包含一个标签，一组数据，一个消息和一个指针。最主要的区别就是 Tag 对象指向一个 commit 而不是一个 tree。
        它就像是一个分支引用，但是不会变化——永远指向同一个 commit，仅仅是提供一个更加友好的名字。
        ```
        $ cat .git/refs/tags/v1.1
        9585191f37f7b0fb9444f35a9bf50de191beadc2
        ```


- tag与commit的关系

- 打标签
    - 何时需要打
    - 怎么打

- 查看有哪些branch merged到了vt2
```
checkout to the branch you want to check, then
$ git pull
$ git branch --merged vt2
```

https://stackoverflow.com/questions/29007821/git-checkout-all-the-files
  - `git checkout -- .`
  - `git reset --hard`

```
$ git pull
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> topic/vzhong/PORSCHE-6163-Update-OSM-client-download-link-to-download-latest-version-on-NFS-mount
```

- head
    - 查看当前head
    - git checkout 到一个新的branch，但是head却是原来的，是这样的吗？

- merge也是一个commit吗？


### Git
- Git
    - git submodule [Chinese: https://www.youtube.com/watch?v=jhl7ruTPV-o]
      - git submodule update --init
      - git submodule add
        - 
      - remove submodule ?
        - rm -r <dir-path>, then git commit
    - Git branch strategy


- 为什么刚pull下来的repo，git branch却不显示全部的branch，只显示一个branch
```
$ git branch
* develop_python3
```
    - https://git-scm.com/book/en/v2/Git-Branching-Branch-Management
        - If you run it with no arguments, you get a simple listing of your current branches


```shell
$ git branch --merged
* vz-test
$ git merge vz-test-8
Updating fff3cff..af2c4ba
Fast-forward
 VERSION.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
vzhongPG3QC:osstpclients vzhong$ cat VERSION.txt
v88
vzhongPG3QC:osstpclients vzhong$ git merge vz-test-8
Already up to date.
vzhongPG3QC:osstpclients vzhong$ git branch --merged      <--- show local merged
* vz-test
  vz-test-8
vzhongPG3QC:osstpclients vzhong$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 257 bytes | 257.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote:
remote: To create a merge request for vz-test, visit:
remote:   https://gitlab.eng.vmware.com/core-build/osstpclients/-/merge_requests/new?merge_request%5Bsource_branch%5D=vz-test
remote:
To https://gitlab.eng.vmware.com/core-build/osstpclients.git
   fff3cff..af2c4ba  vz-test -> vz-test
vzhongPG3QC:osstpclients vzhong$ git branch -r --merged
  ...
  origin/topic/zhiwew/download_source_for_rpm
  origin/vz-test
  origin/vz-test-3
  origin/vz-test-4
  origin/vz-test-6
vzhongPG3QC:osstpclients vzhong$ git branch
  develop_python3
* vz-test
  vz-test-8
  xxxx
vzhongPG3QC:osstpclients vzhong$ git status
On branch vz-test
Your branch is up to date with 'origin/vz-test'.

nothing to commit, working tree clean
vzhongPG3QC:osstpclients vzhong$ git push
Everything up-to-date
vzhongPG3QC:osstpclients vzhong$ git checkout vz-test-8
Switched to branch 'vz-test-8'
vzhongPG3QC:osstpclients vzhong$ git push
fatal: The current branch vz-test-8 has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin vz-test-8

vzhongPG3QC:osstpclients vzhong$ git push --set-upstream origin vz-test-8
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: To create a merge request for vz-test-8, visit:
remote:   https://gitlab.eng.vmware.com/core-build/osstpclients/-/merge_requests/new?merge_request%5Bsource_branch%5D=vz-test-8
remote:
To https://gitlab.eng.vmware.com/core-build/osstpclients.git
 * [new branch]      vz-test-8 -> vz-test-8
Branch 'vz-test-8' set up to track remote branch 'vz-test-8' from 'origin'.
vzhongPG3QC:osstpclients vzhong$
vzhongPG3QC:osstpclients vzhong$ git checkout vz-test
Switched to branch 'vz-test'
Your branch is up to date with 'origin/vz-test'.
vzhongPG3QC:osstpclients vzhong$
vzhongPG3QC:osstpclients vzhong$ git pull
Already up to date.
vzhongPG3QC:osstpclients vzhong$ git branch -r --merged
  ...
  origin/topic/zhiwew/download_source_for_rpm
  origin/vz-test
  origin/vz-test-3
  origin/vz-test-4
  origin/vz-test-6
  origin/vz-test-8     <-----
```

- gitlab squash
  - In gitlab, Squash multi commits as one, in this case, what the comment will be like ?
    - as my experience, the new commit's title is MR's title.
  - git squash
    - https://stackoverflow.com/questions/5189560/how-do-i-squash-my-last-n-commits-together
      - 亲测有效
      ```shell
      git reset --soft HEAD~2
      git commit
      ```
- fast-forward
- git revert

- git 3D
  - Gource

- 丁哥： git merge和git rebase的区别, 切记：永远用rebase

- git pull是针对当前分支还是所有分支？
  - 只针对当前分支，只会拉当前的分支，这种东西一次性更新所有分支，万一有冲突，够你吃一壶。所以基本都是只更新当前分支
    - 你说的不准确，是同步所有的远程分支到本地，只不过只对当前分支进行merge

- git clone repo to specific path
  - 

[gitlab] Squash multi commits as one, in this case, what the comment will be like ?


- What is a changeset in Git?
  - source: https://stackoverflow.com/questions/38648491/what-is-a-changeset-in-git
    - 提问者问题：5个files一次commit，是否这5个文件的修改算一个changeset ?
      - https://en.wikipedia.org/wiki/Changeset
        - In version control software, a changeset (also known as commit and revision)
  
- git branch --set-upstream-to
  - 

- git branch | grep -vw "$MERGE_FROM_BRANCH\|$MERGE_TO_BRANCH" | xargs git branch -D # Delete all other branches


git log --merges -n 1

https://stackoverflow.com/questions/10641361/get-all-files-that-have-been-modified-in-git-branch
  - git diff --name-only <notMainDev> $(git merge-base <notMainDev> <mainDev>)
    - git merge-base
      - Finding When Two Branches First Diverged

$ git diff 66c264a2851cd56c8f2b5ae9b62fee801be145ad

- git index

- git squash commits into one
  - 
- undo `git rebase`

```
 ! [remote rejected] release/vzhong/PORSCHE-5658-setup-python-environment-on-mac-for-osstpclients-b -> release/vzhong/PORSCHE-5658-setup-python-environment-on-mac-for-osstpclients-b (pre-receive hook declined)
error: failed to push some refs to 'git@gitlab.eng.vmware.com:core-build/osstpclients.git'
  -  bare repository
```

- git 是否有GUI类的工具，可以像beyondcompare那样对比文件不同，然后选择某个

```
# git branch
fatal: detected dubious (可疑的) ownership in repository at '/tmp/mount/buildaudit-test-sample'
To add an exception for this directory, call:

        git config --global --add safe.directory /tmp/mount/buildaudit-test-sample
# 
# git config --global --add safe.directory /tmp/mount/buildaudit-test-sample
# 
# git branch
* master
```

- git add -A  &   git add -a


```
$ git push origin topic/vzhong/PORSCHE-6136-Automatically-check-version-upgrade-when-osstp-load-is-executed-1
To gitlab.eng.vmware.com:core-build/osstpclients.git
 ! [rejected]        topic/vzhong/PORSCHE-6136-Automatically-check-version-upgrade-when-osstp-load-is-executed-1 -> topic/vzhong/PORSCHE-6136-Automatically-check-version-upgrade-when-osstp-load-is-executed-1 (non-fast-forward)
error: failed to push some refs to 'git@gitlab.eng.vmware.com:core-build/osstpclients.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

solution:

git stash save
  - 使用场景
    - 
  - stash:
    n.藏匿处；藏匿物
    vt.存放；贮藏
    vi.存放；藏起来


git pull --rebase
From: https://stackoverflow.com/questions/22532943/how-to-resolve-git-error-updates-were-rejected-because-the-tip-of-your-current
```

- How do I force "git pull" to overwrite local files?
    ```
    This will remove all uncommitted changes, even if staged,
    and then pull:

    git reset --hard HEAD
    git pull
    But any local file that's not tracked by Git will not be affected.
    ```
      - git reset --hard HEAD 表示回退到当前版本，HEAD指向当前版本。如果你修改了一些代码，想去除，就可以用git reset --hard HEAD一次性去除

- 将2个不连续的commit合并
  - 亲测有效 https://blog.csdn.net/qq_29518275/article/details/122052289

- 修改 commit的message
  - latest commit
    - git commit --amend
  - 任意一个commit
    - 用一个土办法，随意new 一个 commit, 然后根据'将2个不连续的commit合并': https://blog.csdn.net/qq_29518275/article/details/122052289 去改动特定的commit的message

- .gitmodules

- github pull request


- how to check if a file is git ignored [duplicate]
  - git status 就行了

- Exporting a software bill of materials for your repository
  - https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository
  - SBOM与SPDX的关系
    - sbom
      - https://zhuanlan.zhihu.com/p/595187798

- GitHub Forks and Pull Requests | Step by Step
  - https://www.youtube.com/watch?v=a_FLqX3vGR4
    - 不简洁
  - 什么时候需要用 fork ? 与git clone的区别
    - fork类似于checkout一个新分支，然后修改比如bug，最后合并到主分支
    - fork完后需要merge回origin吗？
      - 一般是要的，pull request合并你的修改
        - 如果我不想merge回呢？我只想拿来改成自己需要的样子
          - `If you want to create a new repository from the contents of an existing repository but don't want to merge your changes to the upstream in the future, you can duplicate the repository or, if the repository is a template, you can use the repository as a template. For more information, see "Duplicating a repository" and "Creating a repository from a template".`
            - https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository
```
# git push -f
fatal: unable to access 'http://github.com/ZhongPengQun2/Shortcuts.git/': gnutls_handshake() failed: The TLS connection was non-properly terminated.
```


### Gitlab
- Tutorials
    - <font color="green">[ Done 60/100 ] </font> 中文tutorial：https://www.bilibili.com/video/BV1Wf4y1p7Xo/?spm_id_from=pageDriver&vd_source=f209dde1a1d76e06b060a034f36bb756
        - 上次观看：https://www.bilibili.com/video/BV1Z64y1r7m9/?spm_id_from=333.788&vd_source=f209dde1a1d76e06b060a034f36bb756
        - Pipeline的类型：DAP, 父子流水线
- Is gitlab free, may it not be free in some future ?
- <font color="green">[ Done 60/100 ] </font>中文tutorial：https://www.bilibili.com/video/BV1Wf4y1p7Xo/?spm_id_from=pageDriver&vd_source=f209dde1a1d76e06b060a034f36bb756
- Gitlab keywords
- Installation
 - docker
 - k8s
- gitlab runner
    - installation: https://www.bilibili.com/video/BV1XK4y1b7Yj/?spm_id_from=333.337.search-card.all.click&vd_source=f209dde1a1d76e06b060a034f36bb756
    - executor
        - docker
    - tag
    - registry


```
The Auto DevOps pipeline has been enabled and will be used if no alternative CI configuration file is found.
Container registry is not enabled on this GitLab instance. Ask an administrator to enable it in order for Auto DevOps to work. 
```
    - CI/CD settings

- gitlab add k8s cluster



GitLab CE Tutorial #5 - Issue Tracking & Milestones
  - https://www.youtube.com/watch?v=tv4UM1ruQRs
  

### Github
github
```shell
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/zhongpengqun/mirror.git/'
```
s: https://stackoverflow.com/questions/68775869/message-support-for-password-authentication-was-removed-please-use-a-personal


- gitlab ipynb



```
C:\Users\zlzk>git clone git@github.com:zhongpengqun/zhongpengqun.github.io.git
Cloning into 'zhongpengqun.github.io'...
kex_exchange_identification: read: Software caused connection abort
banner exchange: Connection to 20.205.243.166 port 22: Software caused connection abort
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

或

C:\Users\zlzk> git clone https://github.com/zhongpengqun/zhongpengqun.github.io.git
Cloning into 'zhongpengqun.github.io'...
fatal: unable to access 'https://github.com/zhongpengqun/zhongpengqun.github.io.git/': Recv failure: Connection was reset

------------
用 github Desktop   https://desktop.github.com/
亲测好用!!
```
