## lsblk命令

### 用法
```
lsblk [options] [<device> ...]
```

| 选项 | 说明 |
| --- | --- |
| -f, --fs | 输出文件系统信息，其中包括UUID，文件系统类型，挂载点,文件系统可用大小等信息。 |
| -p, --paths | 打印完整设备路径 |

### 示例
```shell
# 仅打印挂载点
lsblk /dev/sda1 -n -o MOUNTPOINT

# 打印时加上序列号字段（部分版本没有这个字段）
lsblk -o +serial
```
