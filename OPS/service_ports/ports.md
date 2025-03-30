## 端口&
说明：常见服务的端口及说明

| 端口 | 服务
| --- | ---
| 20            | ftp
| 21            | ftp
| 22            | ssh
| 25            | smtp
| 37            | time
| 53            | dns
| 67            | dhcp
| 69            | tftp
| 80            | http
| 161           | snmp
| 179           | calico
| 443           | https
| 873           | rsync
| 2379          | etcd
| 2380          | etcd
| 3000          | grafana
| 3306          | mysql
| 3389          | rdp
| 5601          | kibana
| 6379          | redis
| 8080          | tomcat 8005(关闭指令端口)
| 9090          | prometheus
| 9092          | kafka
| 9100          | elasticsearch head
| 9200          | elasticsearch         9300(内部节点通信)   
| 30000-32767   | k8s NodePort          
| 6443          | kube-apiserver；用于与 API Server 进行通信
| 10250         | kubelet API；用于与 Kubelet 进行通信。
| 10251         | kube-schedule；用于与 Scheduler 进行通信。
| 10252         | kube-control；用于与 Controller Manager 进行通信
| 10254         | Ingress Controller 健康检查
| 10255         | kubelet API（只读）
| 10256         | kube-proxy
| 10257         | kube-controller-manager
| 10259         | kube-schedule；用于与 Scheduler 进行通信。