# kubectl命令


## kubectl config命令

### 用法
```
kubectl config SUBCOMMAND [options]
```

### 子命令

| current-context | 显示当前context                     |
| --------------- | ----------------------------------- |
| get-contexts    | 显示config中所有context             |
| use-context     | 设置 kubeconfig 文件中的当前context |
|                 |                                     |
|                 |                                     |
|                 |                                     |


---
## kubectl describe命令

### 示例

~~~shell
# 查看节点的污点

~~~

---
## kubectl edit命令


### 示例
~~~shell
# Edit the service named 'docker-registry':
kubectl edit svc/docker-registry

# Use an alternative editor
KUBE_EDITOR="nano" kubectl edit svc/docker-registry

# Edit the job 'myjob' in JSON using the v1 API format:
kubectl edit job.v1.batch/myjob -o json

# Edit the deployment 'mydeployment' in YAML and save the modified config in its annotation:
kubectl edit deployment/mydeployment -o yaml --save-config

~~~

---
## kubectl get命令

| 选项          | 说明             |
| ------------- | ---------------- |
| -A            | 指定所有命名空间 |
| -n            | 指定命名空间     |
| -o            | 指定输出格式     |
|               |                  |
|               |                  |
| --show-labels | 显示资源的标签   |
|               |                  |
|               |                  |

~~~shell
# 以ps输出格式列出所有pod，并提供更多信息(如节点名)。
kubectl get pods -o wide

# 列出指定的replicationcontroller。
kubectl get replicationcontroller web
kubectl get replicationcontroller/web

# 列出所有的命名空间查看所有命名空间：
$ kubectl get namespaces
# List deployments in JSON output format, in the "v1" version of the "apps" API group:
kubectl get deployments.v1.apps -o json

# List a single pod in JSON output format.
kubectl get -o json pod web-pod-13je7

# List a pod identified by type and name specified in "pod.yaml" in JSON output format.
kubectl get -f pod.yaml -o json

# List resources from a directory with kustomization.yaml - e.g. dir/kustomization.yaml.
kubectl get -k dir/

# Return only the phase value of the specified pod.
kubectl get -o template pod/web-pod-13je7 --template={{.status.phase}}

# List resource information in custom columns.
kubectl get pod test-pod -o custom-columns=ONTAINER:.spec.containers[0].name,IMAGE:.spec.containers[0].image

# List all replication controllers and services together in ps output format.
kubectl get rc,services

# List one or more resources by their type and names.
kubectl get rc/web service/frontend pods/web-pod-13je7
~~~

---
## kubectl label命令

### 示例

~~~shell
# 删除一个标签。只需在标签名后面跟一个减号
kubectl label nodes 节点名 标签名-

# 修改一个标签的值
kubectl label nodes --overwrite 节点名 标签名=新值
~~~

---
## kubectl logs命令

### 用法

kubectl logs [-f] [-p] (POD | TYPE/NAME) [-c CONTAINER] [options]

| 选项                  | 说明                                                |
| --------------------- | --------------------------------------------------- |
| -p                    | 容器终止前的日志                                    |
| -f                    | 跟踪日志输出，类似于tail 的-f选项   |
| --tail N              | 查看最后N行日志                                     |
| --all-containers=true | 查看pod中所有容器的日志                             |
| -c CONTAINER          | 当一个pod中有多个容器时，需要加-c选项来指定查看pod中哪个容器的日志。-c init可以查看初始化容器日志 |
| --since=1h            | 查看最近1小时的日志,也可以写10s，5m等            |
| -l app=nginx          | 查看标签app为nginx的日志                            |
| --timestamps          | 输出日志时显示时间戳                            |


### 示例
```shell
# Return snapshot logs from pod nginx with only one container
kubectl logs nginx

# Return snapshot logs from pod nginx with multi containers
kubectl logs nginx --all-containers=true

# Return snapshot logs from all containers in pods defined by label app=nginx
kubectl logs -lapp=nginx --all-containers=true

# Return snapshot of previous terminated ruby container logs from pod web-1
kubectl logs -p -c ruby web-1

# Begin streaming the logs of the ruby container in pod web-1
kubectl logs -f -c ruby web-1

# Display only the most recent 20 lines of output in pod nginx
kubectl logs --tail=20 nginx

# Show all logs from pod nginx written in the last hour
kubectl logs --since=1h nginx

# Return snapshot logs from first container of a job named hello
kubectl logs job/hello

# Return snapshot logs from container nginx-1 of a deployment named nginx
kubectl logs deployment/nginx -c nginx-1
```

---
## kubectl rollout命令

管理一个资源的滚动，有效的资源为：`deployments`、`daemonsets`、`statefulsets`

### 用法

~~~
Available Commands:
  history     显示 rollout 历史
  pause       标记提供的 resource 为中止状态
  restart     Restart a resource
  resume      继续一个停止的 resource
  status      显示 rollout 的状态
  undo        撤销上一次的 rollout
~~~

### 示例
```shell
# 重启名为nginx的deployment
kubectl rollout restart deployment/nginx
```

---
## kubectl set命令

### 示例
~~~shell
#更新一个 pod template 的镜像
kubectl set image
~~~

---
## kubectl taint命令

### 示例

```shell
# 删除master不可调度的污点
kubectl taint node <节点名> node-role.kubernetes.io/master:NoSchedule-
```

---
## kubectl top命令&

显示资源（CPU、内存、存储）的使用情况

### 用法

kubectl top [flags] [options]

### 示例

~~~shell
# 查看所有节点的资源使用情况
kubectl top node

# 查看指定pod的资源使用情况
kubectl top pod -n kube-system kube-apiserver-XXX
~~~
