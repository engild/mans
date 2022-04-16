# git switch命令

切换到指定的分支。工作树和索引被更新以匹配分支。所有新的提交都将添加到这个分支的顶端。

## 用法
```
git switch [<options>] [--no-guess] <branch>
git switch [<options>] --detach [<start-point>]
git switch [<options>] (-c|-C) <new-branch> [<start-point>]
git switch [<options>] --orphan <new-branch>
```

## 示例

```shell
# 切换到上一个分支
git switch -

# 切换到master分支
git switch master
```
