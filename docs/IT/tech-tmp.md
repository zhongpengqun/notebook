https://github.com/joeltennant/Jekyll-and-Docker-Compose
```shell
# docker-compose up
[+] Running 2/2
 ⠿ Network jekyll-and-docker-compose_default     Created                                                                                                                                               0.0s
 ⠿ Container jekyll-and-docker-compose-jekyll-1  Created                                                                                                                                               0.1s
Attaching to jekyll-and-docker-compose-jekyll-1
jekyll-and-docker-compose-jekyll-1  | ruby 3.1.1p18 (2022-02-18 revision 53f5fc4236) [x86_64-linux-musl]
jekyll-and-docker-compose-jekyll-1  |   Logging at level: debug
jekyll-and-docker-compose-jekyll-1  |     Jekyll Version: 4.2.2
jekyll-and-docker-compose-jekyll-1  | Configuration file: /srv/jekyll/_config.yml
jekyll-and-docker-compose-jekyll-1  |   Logging at level: debug
jekyll-and-docker-compose-jekyll-1  |     Jekyll Version: 4.2.2
jekyll-and-docker-compose-jekyll-1  |                     ------------------------------------------------
jekyll-and-docker-compose-jekyll-1  |       Jekyll 4.2.2   Please append `--trace` to the `serve` command 
jekyll-and-docker-compose-jekyll-1  |                      for any additional information or backtrace. 
jekyll-and-docker-compose-jekyll-1  |                     ------------------------------------------------
jekyll-and-docker-compose-jekyll-1  | /usr/local/lib/ruby/3.1.0/fileutils.rb:243:in `mkdir': Permission denied @ dir_s_mkdir - /srv/jekyll/.jekyll-cache (Errno::EACCES)
jekyll-and-docker-compose-jekyll-1  |   from /usr/local/lib/ruby/3.1.0/fileutils.rb:243:in `fu_mkdir'
jekyll-and-docker-compose-jekyll-1  |   from /usr/local/lib/ruby/3.1.0/fileutils.rb:221:in `block (2 levels) in mkdir_p'
jekyll-and-docker-compose-jekyll-1  |   from /usr/local/lib/ruby/3.1.0/fileutils.rb:219:in `reverse_each'
jekyll-and-docker-compose-jekyll-1  |   from /usr/local/lib/ruby/3.1.0/fileutils.rb:219:in `block in mkdir_p'
jekyll-and-docker-compose-jekyll-1  |   from /usr/local/lib/ruby/3.1.0/fileutils.rb:211:in `each'
jekyll-and-docker-compose-jekyll-1  |   from /usr/local/lib/ruby/3.1.0/fileutils.rb:211:in `mkdir_p'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/cache.rb:184:in `dump'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/cache.rb:101:in `[]='
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/cache.rb:45:in `clear_if_config_changed'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/site.rb:118:in `reset'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/site.rb:35:in `initialize'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/commands/build.rb:30:in `new'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/commands/build.rb:30:in `process'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/command.rb:91:in `block in process_with_graceful_fail'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/command.rb:91:in `each'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/command.rb:91:in `process_with_graceful_fail'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/commands/serve.rb:86:in `block (2 levels) in init_with_program'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `block in execute'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `each'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `execute'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/mercenary-0.4.0/lib/mercenary/program.rb:44:in `go'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/mercenary-0.4.0/lib/mercenary.rb:21:in `program'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/gems/jekyll-4.2.2/exe/jekyll:15:in `<top (required)>'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/bin/jekyll:25:in `load'
jekyll-and-docker-compose-jekyll-1  |   from /usr/gem/bin/jekyll:25:in `<main>'
jekyll-and-docker-compose-jekyll-1 exited with code 1
```


- Splunk
    - https://www.youtube.com/watch?v=m95GiTF0zd0
    - https://www.youtube.com/watch?v=bO_-fv6e7u4
    - https://medium.com/airwalk/log-aggregation-in-kubernetes-and-transporting-logs-to-splunk-for-analysis-ad8599607372
    - https://cloud.google.com/architecture/logging-anthos-with-splunk-connect?hl=zh-cn
    - k8s logs
        - objects
        - metrics


setup a splunk server:
```shell
docker run --name splunk -p 8000:8000 -p 8088:8088 -d outcoldman/splunk:6.3.3


docker run --name hello --log-driver=splunk --log-opt splunk-token=022F1FCE-B904-4E0E-B0A1-EB4492F61B9D --log-opt splunk-url=http://139.196.39.92:8088 --log-opt splunk-sourcetype=Docker rickfast/hello-oreilly

docker run --name hello --log-driver=splunk --log-opt splunk-token=1620a639-5064-43dc-8d81-72ae38ec639b --log-opt splunk-url=http://10.79.128.59:8088 --log-opt splunk-sourcetype=Docker rickfast/hello-oreilly
```






```shell
curl -k https://139.196.39.92:8088/services/collector/event -H "Authorization: Splunk C8D04ABF-AE0A-4FEB-935C-9F0751FEA816" -d '{"event": "hello world"}'
```

splunk log success: https://www.youtube.com/watch?v=qROXrFGqWAU&t=11s

curl https://10.79.128.59:8088/services/collector/event -H "Authorization: Splunk 1620a639-5064-43dc-8d81-72ae38ec639b" -d '{"event": "hello world"}'

docker built-in send log to splunk ?
https://www.w3cschool.cn/doc_docker_1_13/docker_1_13-engine-admin-logging-splunk-index.html

install splunk by cmd
https://www.inmotionhosting.com/support/security/install-splunk/

9ED0A79E-F7B8-43DC-B7A0-7B49AE7450B9

```shell
root@iZuf6bpc1lt9qlf2ma9p2lZ:~# helm install anthos-splunk -f values.yaml --namespace splunk-connect https://github.com/splunk/splunk-connect-for-kubernetes/releases/download/1.4.1/splunk-connect-for-kubernetes-1.4.1.tgz

Error: INSTALLATION FAILED: Get "https://github.com/splunk/splunk-connect-for-kubernetes/releases/download/1.4.1/splunk-connect-for-kubernetes-1.4.1.tgz": unexpected EOF
```

```shell
$ kubectl create namespace splunk-connect
$ kubectl config set-context --current --namespace=splunk-connect
$ 
helm install anthos-splunk -f values.yaml --namespace splunk-connect https://github.com/splunk/splunk-connect-for-kubernetes/releases/download/1.4.1/splunk-connect-for-kubernetes-1.4.1.tgz
```


```shell
   58  sudo apt-get install libmysqlclient-dev
   59  sudo apt-get install mysql-server
   60  pip3 install  mysqlclient==2.0.3
```