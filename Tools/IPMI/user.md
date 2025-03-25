## ipmitool user命令
配置BMC的用户

```sh
# 列出所有用户
user list

# 修改id为2的BMC用户密码为ADMIN，用户id使用user list查询
user set password 2 ADMIN
```
