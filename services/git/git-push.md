# git push命令

更新远程引用和相关对象

使用本地refs更新远程refs。

当命令行没有指定使用`<repository>`参数推送的位置时，使用`branch.*`。参考当前分支的远程配置，以确定在何处推送。如果缺少配置，则默认为`origin`。
## 用法
```
git push [--all | --mirror | --tags] [--follow-tags] [--atomic] [-n | --dry-run] [--receive-pack=<git-receive-pack>]
                  [--repo=<repository>] [-f | --force] [-d | --delete] [--prune] [-v | --verbose]
                  [-u | --set-upstream] [-o <string> | --push-option=<string>]
                  [--[no-]signed|--signed=(true|false|if-asked)]
                  [--force-with-lease[=<refname>[:<expect>]]]
                  [--no-verify] [<repository> [<refspec>...]]
```
## 示例

```shell
git push
```
