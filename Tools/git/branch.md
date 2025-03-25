## git branch命令
说明：列出、创建或删除分支

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
```sh
# 列出分支
git branch

# 修改分支名
git branch -m old-branch-name new-branch-name

# 删除temp分支
git branch -d temp

# 强制删除temp分支
git branch -D temp
```
