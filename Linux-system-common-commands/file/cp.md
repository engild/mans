## cp命令

复制文件和目录

### 用法
```
cp [OPTION]... [-T] SOURCE DEST
cp [OPTION]... SOURCE... DIRECTORY
cp [OPTION]... -t DIRECTORY SOURCE...
```

| 选项                | 说明                               |
| ------------------- | ---------------------------------- |
| -f                  | 强制复制                           |
| -l                  | 硬链接文件，而不是复制             |
| -R, -r, --recursive | 递归复制目录及其子目录内的所有内容 |

```shell
# 强制创建软链接
cp -lf /usr/bin/python3 /usr/bin/python
```
