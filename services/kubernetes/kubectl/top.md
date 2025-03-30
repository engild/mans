## kubectl top命令
说明：显示资源（CPU、内存、存储）的使用情况

### 用法

kubectl top [flags] [options]

### 示例

~~~shell
# 查看所有节点的资源使用情况
kubectl top node

# 查看指定pod的资源使用情况
kubectl top pod -n kube-system kube-apiserver-XXX
~~~