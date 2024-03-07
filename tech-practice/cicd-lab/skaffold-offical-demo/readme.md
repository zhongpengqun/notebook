# cd django-postgres-skaffold-k8s
skaffold dev

# cd getting-started
skaffold dev

```shell
 - Error: unknown flag: --wait
Cleaning up resources encountered an error, will continue to clean up other resources.
build [skaffold-example] failed: could not push image "skaffold-example:latest": Error response from daemon: You cannot push a "root" repository. Please rename your repository to docker.io/<user>/<repo> (ex: docker.io/<user>/skaffold-example)
```
then change skaffold.yaml image as `docker.io/zhongpengqun/skaffold-example`, get new error

```
 - Error: unknown flag: --wait
Cleaning up resources encountered an error, will continue to clean up other resources.
Build Failed. No push access to specified image repository. Try running with `--default-repo` flag. Otherwise start a local kubernetes cluster like `minikube`.

[ solution ]
# docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: zhongpengqun
Password: 
Login Succeeded
```

另一种方法，skaffold push到本地cluster, Failed for now !!
```
  local:
    push: false

https://www.saoniuhuo.com/question/detail-2277698.html
```
