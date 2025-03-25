## docker pull命令&

从注册表中提取镜像或存储库拉取镜像

### 用法
```
docker pull [Options] NAME[:TAG|@DIGEST]
```

| 选项 | 说明 |
| --- | --- |
| -q | 不详细输出拉取过程 |
| -a | 下载存储库中所有镜像 |
| --platform | 指定平台 |

### 示例
```shell
# 从默认仓库拉取mysql的最新镜像
docker pull mysql

# 指定平台
docker pull mysql --platform=linux/amd64

# 拉取指定版本的nginx镜像，并且不详细输出拉取过程
docker pull -q nginx:1.17.10


```