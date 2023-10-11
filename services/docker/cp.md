## docker cp命令&

在容器和本地文件系统之间复制文件

### 用法
```sh
# 从容器往本地复制
docker cp [Options] CONTAINER:SRC_PATH DEST_PATH|-

# 从本地往容器复制
docker cp [Options] SRC_PATH|- CONTAINER:DEST_PATH
```

| 选项 | 说明 |
| --- | --- |
| -a | 存档模式（复制所有uid / gid信息） |
| -L | 始终遵循SRC_PATH中的符号链接|

### 示例
```sh
# 将容器nginx中的/etc/hosts文件复制到当前目录
docker cp nginx:/etc/hosts ./
```