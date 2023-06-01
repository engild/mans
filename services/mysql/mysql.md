## mysql命令
### 用法
```
mysql [OPTIONS] [database]
```

| 选项                  | 说明                                                  |
| --------------------- | ----------------------------------------------------- |
| -u, --user=name       | 连接数据库的用户                                      |
| -p, --password[=name] | 密码，-p后面不可以有空格，如果不输入密码将在tty中获取 |
| -P, --port=#          | 端口号                                                |
| -h, --host=name       | 主机                                                  |
| -e, --execute=name    | 执行命令然后退出（非交互式）                          |

### 示例

```shell
# 非交互式显示所有数据库
mysql -e 'show databases;'

# 导入数据库
mysql < all_db.sql
```
