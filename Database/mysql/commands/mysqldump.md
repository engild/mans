## mysqldump命令

转储MySQL数据库和表的结构和内容。

默认选项按照给定的顺序从以下文件中读取:`/etc/my.cnf` ---> `/etc/mysql/my.cnf` --->  `~/.my.cnf`

### 用法
```
mysqldump [OPTIONS] database [tables]
mysqldump [OPTIONS] --databases [OPTIONS] DB1 [DB2 DB3...]
mysqldump [OPTIONS] --all-databases [OPTIONS]
```
| 选项 | 说明                                                  
| --- | ---
| -h, --host=name       | 主机
| -P, --port=#          | 端口号
| -u, --user=name       | 用户
| -p, --password[=name] | 密码，-p后面不可以有空格，如果不输入密码将从标准输入中获取
| -A, --all-databases   | 转储所有数据库
| -B, --databases       | 指定数据库
|                       |

### 示例

~~~shell
# 转储所有数据库
mysqldump -uroot -p -A > /tmp/all_db.sql

# 备份testdb数据库
mysqldump -B testdb > /tmp/all_db.sql

# 导出符合条件的数据
mysqldump DATABASE_NAME TABLE_NAME --where="id = 1234"
~~~
