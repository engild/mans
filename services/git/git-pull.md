# git pull

将远程存储库中的更改合并到当前分支中。

在默认模式下，`git pull`是后面跟着`git fetch`的简写去合并`FETCH_HEAD`。

更准确地说，`git pull`使用给定的参数运行`git fetch`，并调用`git merge`将检索到的分支头合并到当前分支中。使用`--rebase`，它运行`git rebase`而不是`git merge`

\<repository>和\<branch>的默认值是从gitbranch(1)设置的当前分支的“remote”和“merge”配置中读取的。

## 用法
```
git pull [<options>] [<repository> [<refspec>...]]
```
## 示例
```shell
git pull
```
