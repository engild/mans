## docker export命令&
说明：将容器的文件系统导出为`tar`归档文件。

该方式保存的是容器，所以对容器相应的修改也会保存下来。

注：此方式导出的镜像归档文件，需用`docker import`导入，不能用`docker load`

### 用法
```
docker export [Options] CONTAINER
```

| 选项 | 说明 |
| --- | --- |
| -o | 指定镜像导出的位置 |

### 示例
```sh
# 将名为nginx容器导出，保存到当前目录下为nginx.tar
docker export nginx -o nginx.tar
```
