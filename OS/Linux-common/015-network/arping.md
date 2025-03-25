## arping命令

### 用法
```
Usage: arping [-fqbDUAV] [-c count] [-w timeout] [-I device] [-s source] destination
```

| 选项      | 说明               |
| --------- | ------------------ |
| -I device | 使用哪个以太网设备 |
|           |                    |
|           |                    |

### 示例
~~~shell
# 使用eth0网卡，对10.127.100.248发···
arping -I eth0 10.127.100.248
~~~
