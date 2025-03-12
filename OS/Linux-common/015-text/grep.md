## grep命令

### 用法
```
grep [OPTION]... PATTERN [FILE]...
```

| 选项 | 说明 |
| --- | --- |
| -i                        | 忽略大小写 |
| -e, --regexp=PATTERNS     | 指定PATTERN进行匹配，可以写多个-e |
| -E                        | 扩展正则表达式 |
| -w                        | 只匹配整个单词 |
| -x                        | 只匹配整行 |
| -r                        | 递归 |
| -s                        | 不显示错误信息 |
| -v                        | 选中不匹配的行。取反 |
| -m \<NUM>                 | 匹配`NUM`次后停止 |
| -n                        | 打印行号 |
| -H                        | 输出时打印匹配的文件名 |
| -h                        | 输出时不显示文件名前缀 |
| -q                        | 不显示所有常规输出
| -A NUM                    | 打印文本及其后面NUM 行
| -B NUM                    | 打印文本及其前面NUM 行
| -C NUM                    | 打印文本及其前后NUM 行，或者直接-NUM
| -o, --only-matching       | 只打印正则匹配部分
| -P                        | 


### 示例
```shell
# 以‘或’的关系匹配多个条件
grep -E 'x|y'
egrep 'x|y'
grep -e x -e y

# 匹配以'#'开头，以;结尾
grep '^#.*;$'

# 匹配空行
grep ^$

# 匹配一次后就停止
grep -m1 word

# 精确匹配单词。grep是以非下划线进行分词。
echo word | grep -w word   # 成功
echo words | grep -w word   # 失败
echo "hello-world" | grep -w hello   # 成功
echo "hello_world" | grep -w hello   # 失败

# 仅输出正则匹配部分
echo "banana 88" | grep -oP 'banana \K\d+'   # 结果为88

# 过滤数字
grep '[0-9]' filename.txt
```
