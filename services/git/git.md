## git clone命令

将存储库克隆到新建的目录中。

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

```shell
# 克隆https仓库
git clone https://github.com/engild/mans.git

# 克隆指定分支
git clone -b 分支名 仓库地址
```

---
## git switch命令

切换到指定的分支。工作树和索引被更新以匹配分支。所有新的提交都将添加到这个分支的顶端。

### 用法
```
git switch [<options>] [--no-guess] <branch>
git switch [<options>] --detach [<start-point>]
git switch [<options>] (-c|-C) <new-branch> [<start-point>]
git switch [<options>] --orphan <new-branch>
```

### 示例

```shell
# 切换到上一个分支
git switch -

# 切换到master分支
git switch master
```

---
## git remote命令
### 用法
```
git remote [-v | --verbose]
git remote add [-t <branch>] [-m <master>] [-f] [--[no-]tags] [--mirror=<fetch|push>] <name> <url>
git remote rename <old> <new>
git remote remove <name>
git remote set-head <name> (-a | --auto | -d | --delete | <branch>)
git remote set-branches [--add] <name> <branch>...
git remote get-url [--push] [--all] <name>
git remote set-url [--push] <name> <newurl> [<oldurl>]
git remote set-url --add [--push] <name> <newurl>
git remote set-url --delete [--push] <name> <url>
git remote [-v | --verbose] show [-n] <name>...
git remote prune [-n | --dry-run] <name>...
git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
```
### 示例

```shell
# 显示远程仓库信息
git remote -v

# 添加远程仓库
git remote add upstream https://github.com/engild/mans.git

# 重命名远程仓库
git remote rename upstream upstream1

# 删除远程仓库
git remote remove upstream1
```

---
## git status

显示工作树状态

显示索引文件和当前头提交之间有差异的路径，工作树和索引文件之间有差异的路径，以及工作树中Git没有跟踪的路径(gitignore(5)没有忽略的路径)。

第一个是运行git commit要提交的内容;第二个和第三个选项是在运行git commit之前运行git add可以提交的内容。

### 用法

| 选项 | 说明   |
| ---- | ------------|
| -s   | 以短格式输出                                                 |
| -b   | 显示分支和跟踪信息，即使在短格式输出模式                     |
| -v   | 详细模式，除了已经更改的文件名称，还显示暂存以提交的文本更改，如果-v被指定两次，还将显示工作树中还没有被暂存的变化 |

### 示例
```shell
git status -vv

git status -sb
```

---
## git branch命令
列出、创建或删除分支

### 用法
```
git branch [--color[=<when>] | --no-color] [-r | -a]
        [--list] [-v [--abbrev=<length> | --no-abbrev]]
        [--column[=<options>] | --no-column]
        [(--merged | --no-merged | --contains) [<commit>]] [<pattern>...]
git branch [--set-upstream | --track | --no-track] [-l] [-f] <branchname> [<start-point>]
git branch (--set-upstream-to=<upstream> | -u <upstream>) [<branchname>]
git branch --unset-upstream [<branchname>]
git branch (-m | -M) [<oldbranch>] <newbranch>
git branch (-d | -D) [-r] <branchname>...
git branch --edit-description [<branchname>]
```
| 选项 | 说明 |
| ---- | ------------|
| -d   | 删除一个分支。分支必须完全合并到其上游分支中，或者如果没有用--track或--set-upstream设置上游，则在HEAD中合并 |
| -D   | 删除分支，不考虑其合并状态。                                 |
|      |                                                              |
| -r   | 列出远程跟踪分支，配合-d可以删除远程分支。&                  |
| -a   | 列出远程跟踪分支和本地分支。&                                |
| -m   | 移动或者重命名分支和相应的reflog                             |
| -M   | 移动/重命名分支，即使新的分支名称已经存在。                  |

### 示例
```shell
# 列出分支
git branch

# 修改分支名
git branch -m old-branch-name new-branch-name

# 删除temp分支
git branch -d temp

# 强制删除temp分支
git branch -D temp
```

---
## git pull

将远程存储库中的更改合并到当前分支中。

在默认模式下，git pull是后面跟着git fetch的简写去合并FETCH_HEAD。

更准确地说，git pull使用给定的参数运行git fetch，并调用qit merge将检索到的分支头合并到当前分支中。使用--rebase，它运行git rebase而不是git merge

\<repository>和\<branch>的默认值是从gitbranch(1)设置的当前分支的“remote”和“merge”配置中读取的。

### 用法
```
git pull [<options>] [<repository> [<refspec>...]]
```
### 示例
```shell
git pull
```
