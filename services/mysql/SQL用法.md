# SQL

## 基础常用SQL语句示例
```sql
# 从user这个表中，删除age字段
alter table user DROP COLUMN age;
```

## 其他常用SQL语句示例

### 查看每个数据库所占磁盘大小

```sql
# 查看每个数据库所占磁盘大小
select
  table_schema as "库名",
  truncate(sum(`data_length`) / 1024 / 1024, 2) as "表所占空间（mb）",
  truncate(sum(`index_length`) / 1024 / 1024, 2) as "索引所占空间（mb）",
  truncate((sum(`data_length`) + sum(`index_length`)) / 1024 / 1024,2) as "空间累计（mb）"
from
  information_schema.`tables`
group by `table_schema`;
```
SELECT table_name, data_length + index_length AS len, table_rows,
CONCAT(ROUND((data_length + index_length)/1024/1024,2),'MB') AS datas FROM information_schema.tables 
WHERE table_schema = 'database_name' ORDER BY len DESC; # 修改database_name


### 查看所有用户

```sql
select user,host from mysql.user;

-- 或者
SELECT DISTINCT CONCAT('User: ''',user,'''@''',host,''';') AS query FROM mysql.user;
```



## 用法

#### where
| 运算符 | 说明 |
| --- | --- |
| = | 等于 |
| <>, != | 不等于 |
| > | 大于 |
| < | 小于 |
| >= | 大于等于 |
| <= | 小于等于 |

```sql
-- 单条件
select * from table_name where field = 'abc';

-- 多条件 AND
select * from table_name where field1 = 'abc' AND field2 = 'bbb';

-- 多条件 OR
select * from table_name where field1 = 'abc' OR field2 = 'bbb';


```

#### limit
```sql
-- 只显示10行
select * from table_name limit 10;

```


### 函数类

#### count
```sql
select count(*) from table_name;

select count(1) from table_name;



```

#### now
返回当前时间
```sql
show now();


select * from table_name where create_time >= ( NOW( ) - INTERVAL 24 HOUR );

```
#### to_days
返回公元0年到现在的天数
```sql
show to_days(now());

-- 查今天的数据
select * from table_name where to_days(date) = to_days(now());

-- 

select * from table_name where to_days(date) = to_days(now());

```
1、查询当天的数据

select * from 表名 where TO_DAYS(时间字段)=TO_DAYS(NOW());

2、查询当周的数据

select * from 表名 where YEARWEEK(DATE_FORMAT(时间字段,‘%Y-%m-%d’))=YEARWEEK(NOW());

3、查询当月的数据

select * from 表名 where DATE_FORMAT(时间字段,‘%Y%m’)=DATE_FORMAT(CURDATE(),‘%Y%m’);

4、查询昨天的数据

select * from 表名 where TO_DAYS(NOW())-TO_DAYS(时间字段)=1;

5、查询最近7天的数据

select * from 表名 where DATE_SUB(CURDATE(),INTERVAL 7 DAY)<=DATE(时间字段);

6、查询当年的数据

select * from 表名 where YEAR(时间字段) =YEAR(NOW());

7、查询上周的数据

select * from 表名 where YEARWEEK(DATE_FORMAT(时间字段,‘%Y-%m-%d’))=YEARWEEK(NOW())-1;

8、查询上月的数据

select *from 表名

where PERIOD_DIFF(DATE_FORMAT(NOW(),‘%Y%m’),DATE_FORMAT(时间字段,‘%Y%m’)

SELECT a.*, b.* FROM table_a a JOIN table_b b ON a.id = b.id;

select a.host,b.asset_name,c.name,a.create_time from siem_asset_addr_info a join siem_asset_info b join siem_asset_system_type_info c  where a.id=b.id AND b.system_type = c.id AND DATE_SUB(CURDATE(),INTERVAL 30 DAY)<= DATE(a.create_time);