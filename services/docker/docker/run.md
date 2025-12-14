## docker run命令
说明：创建并启动一个容器

`docker run`是`docker create`和`docker start`的组合

### 用法
```
docker run [Options] IMAGE [COMMAND] [ARG...]

选项几乎和docker create一样，只是多了下面几个选项。
```

| 选项 | 说明 |
| --- | --- |
| -d | 后台启动容器，并返回容器ID
