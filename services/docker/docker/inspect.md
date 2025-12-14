## docker inspect命令&
说明：返回docker对象的详细信息

docker对象包括`containers`,`images`,`volume`,`network`等信息

### 用法
```
docker inspect [Options] NAME|ID [NAME|ID...]
```

### 示例
```sh
# 查看容器信息
docker inspect CONTAINERS

# 查看镜像的信息
docker inspect IMAGES
```