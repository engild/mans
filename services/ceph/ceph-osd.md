# ceph osd命令

## 示例

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
