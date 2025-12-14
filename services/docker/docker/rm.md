## docker rm命令&
说明：移除一个或多个容器

### 用法
```
docker rm [Options] CONTAINER [CONTAINER...]
```
| 选项 | 说明 |
| --- | --- |
| -f | 强制移除容器 |
| -v | 删除与容器关联的匿名卷 |

### 示例
```shell
# 强制移除名为nginx的容器
docker rm -f nginx
```
