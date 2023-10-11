## docker ps命令&

列出容器

### 用法
```
docker ps [Options]
```

| 选项 | 说明 |
| --- | --- |
| -a | 显示所有状态的容器（默认仅显示状态为running的） |
| -n | 显示最后创建的N个容器（包括所有状态） |
| -l | 显示最新创建的1容器（包括所有状态） |
| --no-trunc | 不截断容器ID  |
| -q | 只显示容器ID |
| -s | Display total file sizes |

### 示例
```sh
# 显示状态为running的容器
docker ps

# 显示最后创建的10个容器，包括所有状态的
docker ps -n10

# 显示所有状态的容器的ID
docker ps -aq
```