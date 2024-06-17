#### build
- what doese build mean ?


### Agile & Scrum
- What's relationship between Agile & Scrum ?
- epic, https://www.knowledgehut.com/blog/agile/what-is-an-epic-agile, https://www.jianshu.com/p/6ba0034d1a51
- xx

### Software management
<b>What is the Difference Between Build and Release in Software Testing ?</b>

The main difference between Build and Release in Software Testing 

is that Build is a version of a software the development team hands over to the testing team for testing purposes

while Release is a software the testing team hands over to the customer.


<b>what is `deliverable` in software management ?</b>

todo

<b> project vs product </b>

It also leads to another questions

project manager vs product manager
project mindset vs product mindset

<b> inventory </b>

TODO


scrum与waterfall，难道不是只是粒度变细了吗？

differences between `helpnow` and `servicedesk`

### release manage
- fling release


- blue-green deployment

- rc
   - Release Candidate
        - "In Software Versioning: A different approach is to use the major and minor numbers, along with an alphanumeric string denoting the release type, e.g. "alpha" (a), "beta" (b), or "release candidate" (rc)."
            - denoting  标志;预示;象征;表示;意指 
   - What "rc" stands for in the latest Python 3.91rc1 version name [closed]
        - https://stackoverflow.com/questions/65187917/what-rc-stands-for-in-the-latest-python-3-91rc1-version-name
    
- Alpha、Beta、RC、Release版本的区别
    - https://blog.csdn.net/lilongsy/article/details/83094977

    - Alpha
    α是希腊字母的第一个，表示最早的版本，预览版，内部测试版，一般不向外部发布，bug会比较多，功能也不全，一般只有测试人员使用。

    - Beta
    β是希腊字母的第二个，公开测试版，比alpha版本晚些，主要会有“粉丝用户”测试使用，该版本仍然存在很多bug，但比alpha版本稳定一些。这个阶段版本还会不断增加新功能。分为Beta1、Beta2等，直到逐渐稳定下来进入RC版本。

    - RC（Release Candidate）
    最终测试版本，发行候选版本，基本不再加入新的功能，主要修复bug。是最终发布成正式版的前一个版本，将bug修改完就可以发布成正式版了。多数开源软件会推出两个RC版本，最后的 RC2 则成为正式版本。

    - GA（General Availability）
    正式发布的版本；在国外都是用GA来说明release版本的。



### Jira
- transition
- Is it free ?
- How to deploy Jira use docker ?
```shell
docker run --detach --publish 8080:8080 cptactionhank/atlassian-jira:latest
```


### Jfrog
- Installation
helm upgrade --install artifactory --namespace cicd-lab center/jfrog/artifactory

Release "artifactory" does not exist. Installing it now.
Error: repo center not found

s:

- trial edition
https://nonezhong.jfrog.io/ui/repos/tree/General/docker


### kerberos
- https://www.youtube.com/watch?v=5N242XcKAsM


### harbor
https://www.cnblogs.com/gengxiaonuo/p/16840026.html



### minio
- 参考文章
	- https://devopsman.cn/archives/minio-de-ying-yong-chang-jing
- Minio的使用场景？
- Minio中有哪些概念？
	- bucket
	- set
