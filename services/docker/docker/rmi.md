## docker rmi命令&
说明：移除一个或多个镜像

### 用法
```
docker rmi [Options] IMAGE [IMAGE...]
```

| 选项 | 说明 |
| --- | --- |
| -f | 强制移除镜像。镜像被某个窗口使用时需要加该选项。 |

### 示例
```shell
# 删除nginx和mysql镜像
docker rmi nginx mysql

# 强制删除一个镜像
docker rmi -f nginx:1.17.10

# 命令嵌套。删除所有未被使用的镜像
docker rmi `docker images -q`
