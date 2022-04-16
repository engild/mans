# git stash命令

## 示例

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
