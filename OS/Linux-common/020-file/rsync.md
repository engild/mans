## rsync命令
这里写命令的简单说明

### 用法
```
Usage: rsync [OPTION]... SRC [SRC]... DEST
  or   rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST
  or   rsync [OPTION]... SRC [SRC]... [USER@]HOST::DEST
  or   rsync [OPTION]... SRC [SRC]... rsync://[USER@]HOST[:PORT]/DEST
  or   rsync [OPTION]... [USER@]HOST:SRC [DEST]
  or   rsync [OPTION]... [USER@]HOST::SRC [DEST]
  or   rsync [OPTION]... rsync://[USER@]HOST[:PORT]/SRC [DEST]

The ':' usages connect via remote shell, while '::' & 'rsync://' usages connect to an rsync daemon, and require SRC or DEST to start with a module name.
译为：
':'用法通过远程shell连接，而'::' & 'rsync://'用法连接到rsync守护进程，并要求SRC或DEST以模块名开头。

```

| 选项 | 说明
| --- | ---
| -r, --recursive | 递归到目录中
| -t, --times | 保留修改时间
| -e, --rsh=COMMAND | 指定要使用的远程shell
| -z, --compress | 在传输过程中压缩文件数据
| -a, --archive | 归档模式,equals -rlptgoD (no -H,-A,-X)
| --progress |
| --partial |



### 示例
```sh
# 使用非默认22端口的ssh传输
rsync -e "ssh -p 222" /home/dir1 192.168.10.20:/tmp/dir1

```
