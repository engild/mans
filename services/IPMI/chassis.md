## ipmitool chassis命令
这里写命令的简单说明

### 用法
```
xxx [选项]
```

| 选项 | 说明
| --- | ---
|  | 
|  | 
|  | 

### 示例
```sh
# 
chassis status

# 查看电源状态
chassis power status

# 设置磁盘引导
chassis bootdev disk

# 设置pxe引导
chassis bootdev pxe

# 重启后进入bios
chassis bootdev bios
chassis bootparam set bootflag force_bios

# 设置永久disk引导
chassis bootdev disk options=persistent
```
