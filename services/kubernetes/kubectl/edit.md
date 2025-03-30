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