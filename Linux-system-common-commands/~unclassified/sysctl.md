## sysctl命令

### 用法
```
sysctl [options] [variable[=value] ...]
```

| 选项 | 说明                                       |
| ---- | ------------------------------------------ |
| -a   | 显示所有变量                               |
| -p   | 从文件读取变量，配置文件生效               |
| -w   | 允许将值写入变量，-w net.ipv4.ip_forward=1 |
|      |                                            |
