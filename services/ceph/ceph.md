# ceph命令

---
## ceph df命令

### 示例
```shell
ceph df
```

---
## ceph node命令
```shell
# 列出组件的节点
ceph node ls {all|osd|mon|mds|mgr}
```

---
## ceph osd命令

### 示例

~~~shell
# 列出池
ceph osd pool ls [detail]

# 设置pool副本数为2
ceph osd pool set testceph-rbd size 2

# 获取一个池的PG数量
ceph osd pool get <pool-name> <pg_num>

# 获取一个池的PGP数量
ceph osd pool get <pool-name> <pgp_num>

# 增加一个池的PG数量
ceph osd pool set <pool-name> <pg_num number>

# 增加一个池的PGP数量
ceph osd pool set <pool-name> <pgp_num number>
~~~

### 其他示例
```shell
mon is allowing insecure global_id reclaim

ceph config get mon.test-69-onecloud01  auth_allow_insecure_global_id_reclaim

ceph config get mon.test-69-onecloud01  auth_allow_insecure_global_id_reclaim

ceph osd pool get testceph-rbd pg_num
```
