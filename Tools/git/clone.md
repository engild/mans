## git clone命令
说明：将存储库克隆到新建的目录中。

为已克隆存储库中的每个分支创建远程跟踪分支(使用`git branch --remotes`可见)，并创建并签出从已克隆存储库的当前活动分支派生的初始分支。

### 用法

```
git clone [options] [--] <repo> [<dir>]

<repo>   # 远程仓库，仓库地址有ssh、https两种
[<dir>]   # 可选参数，可以指定clone到哪个目录
```

| 选项 | 说明   |
| ---- | ------------|
| -v   | 更详细的输出     |
| -q   | 更安静的输出     |
| -l   | 从本地存储库克隆 |
| -n   |                  |
| -s   | 设置为共享存储库 |
| -o   |                  |

### 示例

```sh
# 克隆https仓库
git clone https://github.com/engild/mans.git

# 克隆指定分支
git clone -b 分支名 仓库地址
```
