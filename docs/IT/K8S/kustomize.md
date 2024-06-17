## kustomize
basic usage: https://www.bilibili.com/video/BV1Gv411b7gy/?spm_id_from=333.337.search-card.all.click&vd_source=f209dde1a1d76e06b060a034f36bb756

https://kustomize.io/
- patchesStrategicMerge
- configmap


### kustomize
- Why Kustomize ?
```shell
xx
```
- Kustomize VS Helm
- Helm DSL syntax ?


- newTag
    - 用来替换所有匹配image的tag

- kustomize edit set image
```
Set an image in the kustomization file:
kustomize edit set image {{busybox=alpine:3.6}}
```

- kustomize build
