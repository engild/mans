## ipmitool命令
这里写命令的简单说明

### 用法
```
xxx [选项]
```

| 选项 | 说明 |
| --- | --- |
| -H | 指定主机 |
| -U | 指定USER |
| -P | 指定密码 |

### 示例
```sh
# 查看BMC硬件信息
ipmitool -H 10.20.33.44 -U admin -P admin mc info

```
