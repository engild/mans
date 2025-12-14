## docker tag命令&
说明：参照一个源镜像来创建一个新的镜像

可以用来修改镜像的名字或者标签，改完后把源镜像删除即可。

### 用法
```
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
```

### 示例
```shell
# 修改tag
docker tag nginx yudeyu/nginx:1.17.10
```