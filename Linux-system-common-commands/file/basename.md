## basename命令&

打印NAME，删除任何主要目录组件。
如果指定，也删除一个尾随SUFFIX。

### 用法
```shell
basename NAME [后缀]
basename 选项... NAME..

```

| 选项 | 说明 |
| --- | --- |
| -a, --multiple | 支持多个参数并将每个参数作为一个NAME |
| -s, --suffix=SUFFIX | 删除尾随后缀;意味着同时使用了-a选项 |
| -z, --zero | 用NUL结束每个输出行，而不是换行符。不换行输出 |

### 示例
```sh
# 同时删除 .bak 后缀
basename /data/test_file.bak .bak
basename -s .bak /data/test_file.bak

# 多个目录，不换行输出
basename -az /data/test1 /data/test2

# 多个目录，且删除 .bak 后缀
basename -s .bak /data/test1.bak /data/test2.bak

```