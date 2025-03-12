## mount命令
这里写命令的简单说明

### 用法
```
xxx [选项]
```

| 选项 | 说明
| --- | ---
| -a, --all | 
| -r, --read-only | 只读挂载（等同于 -o ro）
| -t, --types <list> | 限制文件系统类型的集合

### 示例
```sh
# 查看挂载时的参数
mount | grep /mnt

mount -o ro -t ntfs /dev/sdk2 /home/dir1

```
