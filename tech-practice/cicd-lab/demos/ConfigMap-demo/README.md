refer to https://www.jianshu.com/p/d834bca35c18



```shell
kubectl create -f cm-appvars.yaml
# 查看ConfigMap列表
kubectl get configmap
# 查看ConfigMap cm-appvars
kubectl describe configmap cm-appvars
# 以yaml的形式输出cm-appvars
kubectl get configmap cm-appvars -o yaml
```