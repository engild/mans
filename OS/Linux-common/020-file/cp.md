## cp命令&
说明：复制文件和目录

### 用法
```
cp [OPTION]... [-T] SOURCE DEST
cp [OPTION]... SOURCE... DIRECTORY
cp [OPTION]... -t DIRECTORY SOURCE...
```

| 选项                | 说明                               |
| ------------------- | ---------------------------------- |
| -a, --archive | 等同于 -dR --preserve=all  |
| -d |  |
| -R, -r, --recursive | 递归复制目录及其子目录内的所有内容 |
| --perserve | |
| -f                  | 强制复制                           |
| -s                  | 创建 软 链接文件，而不是复制             |
| -l                  | 创建 硬 链接文件，而不是复制             |
| -u, --update | 仅在源文件比目标文件更新或目标文件丢失时复制 |
| -t, --target-directory=DIRECTORY | 复制所有文件到DIRECTORY |

### 示例

```shell
# 强制创建软链接
cp -sf /usr/bin/python3 /usr/bin/python

# 快速备份，保留原有属主属组等信息。目录也可以使用该方式
cp -a filename{,.bak}

# 复制多个文件到cc这个目录中
cp aa bb cc
cp aa -t cc bb


```
