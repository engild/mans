## ipmitool命令
这里写命令的简单说明

### 用法
```
xxx [选项]
```

| 选项 | 说明 |
| --- | --- |
| -U | 指定USER |
| -P | 指定密码 |
| -I | 
| -H | 指定主机 |

### 示例
```sh
# 查看BMC硬件信息
ipmitool -H 10.20.33.44 -U $USER -P $PASSWORD mc info

```
