## 示例

```shell
# 打印某一时间段的日志，需要以下两个时间点在日志中存在
sed -n '/[2022-4-1 21:02:53/,/2022-4-1 22:59:57/p' test.log

# centos关闭selinux
sed -i 's/^ *SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
```