## route命令


### 用法
```
route [选项]
```

| 选项 | 说明 |
| --- | --- |
|  |  |
|  |  |
|  |  |

### 示例
```sh
# 添加基于网关IP的路由
route add -net 1.1.1.0/24 192.168.1.1
route add -host 192.168.8.9 192.168.1.1

# 根据主机删除路由
route delete -host 192.168.8.9

# 根据网段删除路由
route delete -net 192.168.1.0/24

# 添加默认路由
route add default gw 192.168.2.1

# 删除默认路由
route del default gw 192.168.2.1 ???

# 查看默认路由
route get 0.0.0.0

# 查看到172.16.10.20的路由
route get 172.16.10.20

```
