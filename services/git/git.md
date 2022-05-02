## git命令

### 用法
```
git [--version] [--help] [-C <路径>] [-c <名称>=<取值>]
           [--exec-path[=<路径>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<路径>] [--work-tree=<路径>] [--namespace=<名称>]
           <命令> [<参数>]
```

常见的 Git 命令：
```
开始一个工作区（参见：git help tutorial）
   clone             克隆仓库到一个新目录
   init              创建一个空的 Git 仓库或重新初始化一个已存在的仓库

在当前变更上工作（参见：git help everyday）
   add               添加文件内容至索引
   mv                移动或重命名一个文件、目录或符号链接
   restore           恢复工作区文件
   rm                从工作区和索引中删除文件
   sparse-checkout   初始化及修改稀疏检出

检查历史和状态（参见：git help revisions）
   bisect            通过二分查找定位引入 bug 的提交
   diff              显示提交之间、提交和工作区之间等的差异
   grep              输出和模式匹配的行
   log               显示提交日志
   show              显示各种类型的对象
   status            显示工作区状态

扩展、标记和调校您的历史记录
   branch            列出、创建或删除分支
   commit            记录变更到仓库
   merge             合并两个或更多开发历史
   rebase            在另一个分支上重新应用提交
   reset             重置当前 HEAD 到指定状态
   switch            切换分支
   tag               创建、列出、删除或校验一个 GPG 签名的标签对象

协同（参见：git help workflows）
   fetch             从另外一个仓库下载对象和引用
   pull              获取并整合另外的仓库或一个本地分支
   push              更新远程引用和相关的对象
```

## git add命令
添加文件内容至索引
### 示例
```shell
# 添加所有文件内容至索引
git add .

# 添加指定文件内容至索引
git add <file> ...
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
## git checkout命令

### 用法
```
git checkout [-q] [-f] [-m] [<branch>]
git checkout [-q] [-f] [-m] --detach [<branch>]
git checkout [-q] [-f] [-m] [--detach] <commit>
git checkout [-q] [-f] [-m] [[-b|-B|--orphan] <new_branch>] [<start_point>]
git checkout [-f|--ours|--theirs|-m|--conflict=<style>] [<tree-ish>] [--] <pathspec>...
git checkout [-f|--ours|--theirs|-m|--conflict=<style>] [<tree-ish>] --pathspec-from-file=<file> [--pathspec-file-nul]
git checkout (-p|--patch) [<tree-ish>] [--] [<pathspec>...]
```

### 示例

```shell
# 从upstream/master更新一个路径
git checkout upstream/master --  main.yml

# 从索引区更新一路径
git checkout -- debug.yml
```

---
## git clean命令

### 示例

```shell
git clean -fd
```

---
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
## git commit命令
记录变更到仓库

### 用法
```
git commit [options] [--] <pathspec>...

| 选项 | 说明 |
| --- | --- |
| -q | |
| -v | |
| -m <msg> | 使用给出的<msg>作为提交消息。如果给出多个-m选项，它们的值将作为单独的段落连接起来。-m选项与-c、-C和-F相互排斥。 |
| -a | 提交所有更改的文件 |
| -i | 将指定的文件添加到提交索引中-。 |
| -o | 只提交指定文件 |
```

### 示例

```shell
#
git commit -m "提交说明"

#
git commit -am "提交说明"

git commit --amend --reset-author

```

---
## git config命令

### 示例
```shell
# 修改全局配置文件
git config --global --edit
```

---
## git diff命令
显示提交之间、提交和工作区之间等的差异

---
## git fetch命令
从另外一个仓库下载对象和引用

---
## git log命令
显示commit（提交）日志。

### 用法
| 选项 | 说明 |
| --- | --- |
| --oneline | 一行显示 |

### 示例
```shell
git log --oneline
```

---
## git merge命令
合并两个或更多开发历史
### 示例

```shell
# 把temp分支合并到当前分支
git merge temp
```

---
## git pull命令

将远程存储库中的更改合并到当前分支中。

在默认模式下，`git pull`是后面跟着`git fetch`的简写去合并`FETCH_HEAD`。

更准确地说，`git pull`使用给定的参数运行`git fetch`，并调用`git merge`将检索到的分支头合并到当前分支中。使用`--rebase`，它运行`git rebase`而不是`git merge`

\<repository>和\<branch>的默认值是从gitbranch(1)设置的当前分支的“remote”和“merge”配置中读取的。

### 用法
```
git pull [<options>] [<repository> [<refspec>...]]
```
### 示例
```shell
git pull
```

---
## git push命令

更新远程引用和相关对象

使用本地refs更新远程refs。

当命令行没有指定使用`<repository>`参数推送的位置时，使用`branch.*`。参考当前分支的远程配置，以确定在何处推送。如果缺少配置，则默认为`origin`。
### 用法
```
git push [--all | --mirror | --tags] [--follow-tags] [--atomic] [-n | --dry-run] [--receive-pack=<git-receive-pack>]
                  [--repo=<repository>] [-f | --force] [-d | --delete] [--prune] [-v | --verbose]
                  [-u | --set-upstream] [-o <string> | --push-option=<string>]
                  [--[no-]signed|--signed=(true|false|if-asked)]
                  [--force-with-lease[=<refname>[:<expect>]]]
                  [--no-verify] [<repository> [<refspec>...]]
```
### 示例

```shell
git push
```

---
## git rebase命令
在另一个提交的基础上重新提交
### 用法
```
git rebase [-i | --interactive] [<options>] [--exec <cmd>]
               [--onto <newbase> | --keep-base] [<upstream> [<branch>]]
git rebase [-i | --interactive] [<options>] [--exec <cmd>] [--onto <newbase>]
               --root [<branch>]
git rebase (--continue | --skip | --abort | --quit | --edit-todo | --show-current-patch)
```

### 示例
```shell
git rebase
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
## git reset命令
```
<commit_id>用git log可以查
```
### 示例

```shell
git reset HEAD^

# 回滚到某一次提交，此次提交之后的修改会被退回到暂存区
git reset --soft <commit_id>

# 回滚到某一次提交，此次提交之后的修改不会有任何保留，用git status查看是没有记录的。
git reset --hard <commit_id>
```

---
## git restore命令
恢复工作区文件
### 示例

```shell
# 取消暂存
git restore --staged <文件>...
```

---
## git revert命令

---
## git rm命令
从索引中、或者工作树及索引中，移除指定路径的文件。

### 示例
```shell
git rm hosts
git rm --cache hosts
```

---
## git stash命令

### 示例

```shell
# 储存修改
git stash

# 列出
git stash list

# 恢复
git stash apply

# 恢复到stash@{0}
git stash apply stash@{0}

# 删除
git stash drop

# 恢复并删除，等于git stash apply然后git stash drop
git stash pop
```

---
## git status命令

显示工作树状态

显示索引文件和当前头提交之间有差异的路径，工作树和索引文件之间有差异的路径，以及工作树中Git没有跟踪的路径(gitignore(5)没有忽略的路径)。

第一个是运行`git commit`要提交的内容;第二个和第三个选项是在运行`git commit`之前运行`git add`可以提交的内容。

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
