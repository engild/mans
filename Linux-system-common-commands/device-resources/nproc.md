## nproc命令

打印当前进程可用的处理器数

### 用法
```
nproc [选项]...
```

| 选项       | 说明                        |
| ---------- | --------------------------- |
| --all      | 打印所拥有的处理器数目      |
| --ignore=N | 可能的话，排除 N 个处理单元 |

### 示例

~~~shell
# 查看cpu核心数
nproc --all

nproc --ignore=2

# 忽略两核cpu
nproc --all --ignore=2
~~~
