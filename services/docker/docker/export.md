## docker export命令&
说明：将容器的文件系统导出为tar归档文件。

该操作保存的是容器，所以在容器内的修改也会保存下来。此方式导出的镜像归档文件，需用`docker import`导入，不能用`docker load`

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
