## docker exec命令&
说明：在运行的容器中运行命令

### 用法
```
docker exec [Options] CONTAINER COMMAND [ARG...]

CONTAINER可以是容器的名字，也可以是容器的ID
```

| 选项 | 说明 |
| --- | --- |
| -i | 让容器的标准输入保持打开(即交互式)。 |
| -t | 让 Docker分配一个伪终端（pseudo-tty）并绑定到容器的标准输入上 |
| -e | 设置环境变量。例如：-e E1=1 |
| -w | 设置容器的工作目录。例如：-w /etc |
| -u | 指定用户，可以写用户名或UID |

### 示例
```shell
# 打印nginx这个容器的PATH变量
docker exec nginx echo $PATH

# 进入到centos这个容器当中
docker exec -it centos bash
```

