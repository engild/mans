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

~~~shell
# 非交互式显示所有数据库
mysql -e 'show databases;'

# 导入数据库
mysql < all_db.sql
~~~

## 基础常用SQL语句示例
~~~mysql
# 从user这个表中，删除age字段
alter table user DROP COLUMN age;
~~~

## 其他常用SQL语句示例

### 查看每个数据库所占磁盘大小

~~~sql
select
  table_schema as "库名",
  truncate(sum(`data_length`) / 1024 / 1024, 2) as "表所占空间（mb）",
  truncate(sum(`index_length`) / 1024 / 1024, 2) as "索引所占空间（mb）",
  truncate((sum(`data_length`) + sum(`index_length`)) / 1024 / 1024,2) as "空间累计（mb）"
from
  information_schema.`tables`
group by `table_schema`;
~~~

### 查看所有用户

~~~sql
select user,host from mysql.user;

# 或
SELECT DISTINCT CONCAT('User: ''',user,'''@''',host,''';') AS query FROM mysql.user;
~~~
