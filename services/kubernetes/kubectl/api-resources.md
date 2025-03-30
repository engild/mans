## kubectl api-resources命令
说明：打印支持的API资源

### 常用资源
| 资源名                         | 简写       | 资源分类              | 说明        
| ---                           | ---       | ---                  | ---
| pods                          | po	    | 工作负载型资源         | 
| deployments                   | deploy	| 工作负载型资源         |
| statefulsets                  | sts	    | 工作负载型资源         |
| replicasets                   | rs	    | 工作负载型资源         | 维护一组稳定的 `Pod` 副本，确保在任何时候都有指定数量的 `Pod` 在运行。
| daemonsets                    | ds	    | 工作负载型资源         | 确保所有（或某些）节点上运行一个Pod的副本。常用于运行集群范围内的守护进程，如日志收集、监控代理等。
| jobs                          |           | 工作负载型资源         | 用于运行一次性任务，直到任务成功结束。
| cronjobs                      | cj	    | 工作负载型资源         | 基于时间表的Job，用于定期执行任务。
| services                      | svc       | 服务发现及负载均衡型资源 | 主要工作在四层（传输层），基于TCP/UDP协议，提供基本的负载均衡和服务发现功能。
| ingresses                     | ing	    | 服务发现及负载均衡型资源 | 工作在七层（应用层），基于HTTP/HTTPS协议，提供更高级的路由功能。
| configmaps                    | cm	    | 特殊类型的存储卷        |
| secrets                       |           | 特殊类型的存储卷        |
| namespaces                    | ns        | 集群级资源             | 命名空间
| nodes                         | no	    | 集群级资源             | 工作负载节点
| ClusterRole                   |           | 集群级资源             | 
| endpoints                     | ep	    | 
| priorityclasses               | pc	    |
| storageclasses                | sc	    |
| persistentvolumeclaims        | pvc	    |
| persistentvolumes             | pv	    |
| componentstatuses             | cs	    |
| events                        | ev	    |
| limitranges                   | limits	|
| replicationcontrollers        | rc	    |
| resourcequotas                | quota	    |
| serviceaccounts               | sa	    |
| customresourcedefinitions     | crd,crds	|
| horizontalpodautoscalers      | hpa	    |
| certificatesigningrequests    | csr		|
| networkpolicies               | netpol	|
| poddisruptionbudgets          | pdb	    |
| podsecuritypolicies           | psp	    |