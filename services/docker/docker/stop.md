## docker stop命令&
说明：停止运行一个或多个容器

### 用法
```
docker stop [Options] CONTAINER [CONTAINER...]
```

| 选项 | 说明 |
| --- | --- |
| -t | 在杀死容器之前等待的秒数（默认为10）。指容器不能正常停止，需要强制杀死所等待的时间。 |

### 示例
```shell
# 将名为nginx的容器停止
docker stop nginx
```