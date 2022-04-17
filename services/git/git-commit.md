# git commit命令
记录变更到仓库

## 用法
git commit [options] [--] \<pathspec>...

| 选项 | 说明 |
| --- | --- |
| -q | |
| -v | |
| -m \<msg> | 使用给出的<msg>作为提交消息。如果给出多个-m选项，它们的值将作为单独的段落连接起来。-m选项与-c、-C和-F相互排斥。 |
| -a | 提交所有更改的文件 |
| -i | 将指定的文件添加到提交索引中-。 |
| -o | 只提交指定文件 |

## 示例

```shell
# 
git commit -m "提交说明"

# 
git commit -am "提交说明"

git commit --amend --reset-author

```
