## ipmitool chassis命令
获取机箱状态及设置电源状态

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

# 设置永久disk引导（测试不生效）
chassis bootdev disk options=persistent

# 查看上次系统重启的原因
chassis restart_cause

# 
chassis bootparam get 5
```

# none
Boot parameter version: 1
Boot parameter 5 is valid/unlocked
Boot parameter data: 0000000000
 Boot Flags :
   - Boot Flag Invalid
   - Options apply to only next boot
   - BIOS PC Compatible (legacy) boot 
   - Boot Device Selector : No override
   - Console Redirection control : System Default
   - BIOS verbosity : Console redirection occurs per BIOS configuration setting (default)
   - BIOS Mux Control Override : BIOS uses recommended setting of the mux at the end of POST


# disk
Boot parameter version: 1
Boot parameter 5 is valid/unlocked
Boot parameter data: 8008000000
 Boot Flags :
   - Boot Flag Valid
   - Options apply to only next boot
   - BIOS PC Compatible (legacy) boot 
   - Boot Device Selector : Force Boot from default Hard-Drive
   - Console Redirection control : System Default
   - BIOS verbosity : Console redirection occurs per BIOS configuration setting (default)
   - BIOS Mux Control Override : BIOS uses recommended setting of the mux at the end of POST

# bios
Boot parameter version: 1
Boot parameter 5 is valid/unlocked
Boot parameter data: 8018000000
 Boot Flags :
   - Boot Flag Valid
   - Options apply to only next boot
   - BIOS PC Compatible (legacy) boot 
   - Boot Device Selector : Force Boot into BIOS Setup
   - Console Redirection control : System Default
   - BIOS verbosity : Console redirection occurs per BIOS configuration setting (default)
   - BIOS Mux Control Override : BIOS uses recommended setting of the mux at the end of POST