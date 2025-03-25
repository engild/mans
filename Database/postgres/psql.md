## psql命令
### 用法
```
psql [OPTION]... [DBNAME [USERNAME]]
```
| 选项 | 说明 |
| --- | --- |
| -c | 只运行一个命令（SQL或者内部命令）然后退出 |
| f | 从文件中执行命令，然后退出 |
| -d | 要连接的数据库名 |
| -l | 列出可用数据库，然后退出 |
| -v, --set=, --variable=NAME=VALUE | 设置变量，例如-v ON_ERROR_STOP=1 |
| -V | 显示版本，然后退出 |
| -？ | 显示帮助，然后退出 |
| -h | 数据库主机，或者套接字目录，默认local socket |
| -p | 数据库端口号，默认5432 |
| -U | 数据库用户，默认是当前用户 |
| -w | 永不提示输入密码 |
| -W | 强制提示输入密码 |
	
### 内部命令
psql程序有一些不属于SQL命令的内部命令。它们以反斜线开头，“\”。 欢迎信息中列出了一些这种命令。
| 命令 | 说明 |
| --- | --- |
| \h | 显示帮助 |
| \q | 退出数据库 |
| \l | 显示所有数据库 |
| \dt | 显示所有表 |
| \c | 切换数据库。\c dbname [user] |

### SQL
#### 创建数据库
#### 删除数据库
#### 创建表
```sql
CREATE TABLE weather (
    city            varchar(80),
    temp_lo         int,           -- 最低温度
    temp_hi         int,           -- 最高温度
    prcp            real,          -- 湿度
    date            date
);
```
#### 删除表
```sql
DROP TABLE tablename;
```
#### 插入数据
```sql
INSERT INTO weather VALUES ('San Francisco', 46, 50, 0.25, '1994-11-27');

INSERT INTO weather (date, city, temp_hi, temp_lo)
VALUES ('1994-11-29', 'Hayward', 54, 37);

INSERT INTO weather (city, temp_lo, temp_hi, prcp, date)
VALUES ('San Francisco', 43, 57, 0.0, '1994-11-29')
```
#### 查询表
```sql
# 查询所有列
SELECT * FROM weather;

# 查询指定列
SELECT city, temp_lo, temp_hi, prcp, date FROM weather;

# 消除重复的行
SELECT DISTINCT city FROM weather;

# 使用表达式
SELECT city, (temp_hi+temp_lo)/2 AS temp_avg, date FROM weather;

# 结果排序，以city列正向排序：
SELECT * FROM weather ORDER BY city;
```
#### 多表连接查询
```sql
# 从weather和cities两个表中，查询city是name的行。
SELECT *
    FROM weather, cities
    WHERE city = name;
```
