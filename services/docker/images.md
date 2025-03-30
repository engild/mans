## docker images命令&
说明：列出镜像

### 用法
```
docker images [Options] [REPOSITORY[:TAG]]
```

| 选项 | 说明 |
| --- | --- |
| -a | 显示所有镜像(默认隐藏中间镜像) |
| -q | 只显示镜像的ID。 |
| --no-trunc | 不截断输出。可以显示镜像完整ID。 |

### 示例
```sh
# 查看本地镜像
docker images

# 查看镜像，只显示镜像ID
docker images -q
```
