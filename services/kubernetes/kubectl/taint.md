## kubectl taint命令
说明：更新一个或多个节点上的污点


### 示例

```shell
# 删除master不可调度的污点
kubectl taint node <节点名> node-role.kubernetes.io/master:NoSchedule-
```