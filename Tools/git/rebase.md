## git rebase命令
说明：在另一个提交的基础上重新提交

### 用法
```
git rebase [-i | --interactive] [<options>] [--exec <cmd>]
               [--onto <newbase> | --keep-base] [<upstream> [<branch>]]
git rebase [-i | --interactive] [<options>] [--exec <cmd>] [--onto <newbase>]
               --root [<branch>]
git rebase (--continue | --skip | --abort | --quit | --edit-todo | --show-current-patch)
```

### 示例
```sh
git rebase
```
