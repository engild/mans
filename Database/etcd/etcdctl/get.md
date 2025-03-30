## etcdctl get命令
说明：查询key的值


### 用法
```
etcdctl get [command options] <key>
```

| 选项 | 说明
| --- | ---
| --sort        | 返回结果排序
| --quorum, -q  | 

### 示例
```sh
# 查询 your_key_name 的值
etcdctl get your_key_name


# 通过前缀查询
etcdctl put key01 value01
etcdctl put key02 value02
etcdctl put key/sub1 sub01
etcdctl get key --prefix
```
