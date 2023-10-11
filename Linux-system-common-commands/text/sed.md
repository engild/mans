## sed命令

### 用法
```
sed [选项]... {脚本(如果没有其他脚本)} [输入文件]...
```

| 选项                            | 说明                                     |
| ------------------------------- | ---------------------------------------- |
| -n, --quiet, --silent           | 取消自动打印模式空间                     |
| -i[扩展名], --in-place[=扩展名] | 直接修改文件（如果指定扩展名则备份文件） |
| -e 脚本, --expression=脚本      |                                          |


### 示例

```sh
# 打印第5行
sed -n '5p' testfile

# 替换每行中第一个匹配项
sed 's/a/b/' testfile

# 整行替换
sed 's/a/b/g' testfile

# 使用多个脚本
sed  -e 's/a/b/' -e 's/b/c/' testfile

# 替换换行符为空格
sed ':a;N;$!ba;s/\n/ /g'

# 打印某一时间段的日志，需要以下两个时间点在日志中存在
sed -n '/2022-4-1 21:02:53/,/2022-4-1 22:59:57/p' test.log

# centos关闭selinux
sed -i 's/^ *SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config

# 行首添加字符
sed "s/^/#/"
```
