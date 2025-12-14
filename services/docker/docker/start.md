## docker start命令&
说明：启动一个或多个容器

### 用法

docker start [Options] CONTAINER [CONTAINER...]

| 选项 | 说明 |
| --- | --- |
| -a | 绑定容器的输出 |
| -i | 绑定标准输入 |

### 示例
```shell
# 启动nginx mysql容器
docker start nginx mysql
```
