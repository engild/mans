# git reset命令

## 示例
\<commit_id>用git log可以查
```shell
git reset HEAD^

# 回滚到某一次提交，此次提交之后的修改会被退回到暂存区
git reset --soft <commit_id>

# 回滚到某一次提交，此次提交之后的修改不会有任何保留，用git status查看是没有记录的。
git reset --hard <commit_id>
```
