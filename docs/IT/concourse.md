## Todos
- Offical doc https://concourse-ci.org/examples.html

## Hardware minimum requirement
x

## Concourse
https://concourse-ci.org/resources.html
- resource_types、resources、var_sources、groups、jobs
    - resource_types vs resources
        - https://stackoverflow.com/questions/56337301/concourse-what-is-the-difference-between-resource-types-and-resource
            - resource_type like Class, resource like object
    - resources -> source -> url 什么意思？
      - 当 resources type 为 gitlab 时， url表示gitlab server的地址
      


- Practice

- minimum_succeeded_builds

- 有哪些内置的 resource_type ?

- gitlab integrate concourse

- set_pipeline
  - 

### Concourse
- What is concourse target, why fly -t (target) ?
  - $ fly --target example login --team-name my-team --concourse-url https://ci.example.com
- is concourse pipeline yaml file independent of concourse instance ? i mean a yaml file is able to run everywhere.
- groups
  - x
- var_sources
- inputs
- reveal: true
- in_parallel
- input_mapping / output_mapping
  - official explanation
    - https://concourse-ci.org/exploring-task-input-and-output-scenarios.html#3---mapping-the-names-of-inputs-and-outputs
    - why input_mapping and output_mapping ?
    ```
    Sometimes the names of inputs and outputs don't match between multiple task configs, or they do match and you don't want them overwriting each other, like in the previous example. That's when input_mapping and output_mapping become helpful. 
    ```
    - inputs
    - outputs
- plan vs task
- get
- put
- source type: `gitlab`
  - webhook

- jobs
  - plan
    - task

- Adventage
  - Config file is complete yaml, so it can be managed by git or other version controller.
- Short-coming
  - Yaml file too long.
  - Is there any thing can generate concourse yaml file?


- Specific Runner VS Shared Runner VS Group Runner
  - Specific Runner
    - A certain project to use a specific Runner
      - How to specific a runner to a certain project ?
  - Shared Runner
    - x
  - Group Runner
    - xx

  - Is it possible that register a local machine as a runner ?
  - multiple runners in one project
  - Can we have multiple runners with a single job?

- What's runner's executor ?
- try ... ensure ...
- .git/merge-request.json

- deploy

```shell
$ helm repo add bitnami https://charts.bitnami.com/bitnami
"bitnami" already exists with the same configuration, skipping
$ helm install my-release bitnami/concourse
------output
NAME: my-release
LAST DEPLOYED: Wed Nov 23 15:52:21 2022
NAMESPACE: kube-ops
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: concourse
CHART VERSION: 2.0.0
APP VERSION: 7.8.3

** Please be patient while the chart is being deployed **
###############################################################################
### ERROR: You did not provide an external host in your 'helm install' call ###
###############################################################################

This deployment will be incomplete until you configure Concourse with a resolvable
host. To configure Concourse with the URL of your service:

1. Get the Concourse URL by running:

  NOTE: It may take a few minutes for the LoadBalancer IP to be available.
        Watch the status with: 'kubectl get svc --namespace kube-ops -w my-release-concourse-web'

    export APP_HOST=$(kubectl get svc --namespace kube-ops my-release-concourse-web --template "{{ range (index .status.loadBalancer.ingress 0) }}{{ . }}{{ end }}")

2. Complete your Concourse deployment by running:
    export LOCAL_USERS=$(kubectl get secret --namespace "kube-ops" my-release-concourse-web -o jsonpath="{.data.local_users}" | base64 -d)
    helm upgrade --namespace kube-ops my-release my-repo/concourse \
      --set secrets.localUsers=$LOCAL_USERS \
      --set service.web.type=LoadBalancer \
      --set web.externalUrl=$APP_HOST
```

##### 如何调试concourse，当某个task failed的时候，比如 e2e-test failed 的时候，能否进入到host中去rerun失败了的test？
  - 如何进入 concourse 的 build ？
