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
# 查看电源状态
chassis power status

# 设置磁盘引导
chassis bootdev disk

# 设置pxe引导
chassis bootdev pxe

# 重启后进入bios
chassis bootdev bios

# 强制修改启动项，让机器重启后自动进入BIOS设置界面
chassis bootparam set bootflag force_bios
```
