## docker restart命令
说明：重启一个或多个容器。

### 用法
```
docker restart [Options] CONTAINER [CONTAINER...]
```

| 选项 | 说明 |
| --- | --- |
| -t | 在杀死容器之前等待的秒数（默认为10）。指容器不能正常停止，需要强制杀死所等待的时间。 |

### 示例
```shell
# 重启容器
docker restart mysql
```
