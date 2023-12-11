## cut命令
将每个FILE中选定的行部分打印到标准输出,如果没有FILE，或者FILE为-，则读取标准输入

### 用法
```
cut 选项... [FILE]...
```

| 选项 | 说明 |
| --- | --- |
| -d, --delimiter=DELIM | 指定分隔符，默认是用TAB |
| -f, --fields=LIST |  |
|  |  |

### 示例
```sh
# 以 : 分隔，打印第二个字段
cut -d : -f2

# 以 . 分隔，打印1到3字段，会包括分隔符
cut -d'.' -f1-3

```