## nc命令
连接或监听任意TCP或者UDP

### 用法
```shell
nc [-46CDdFhklNnrStUuvZz] [-I length] [-i interval] [-M ttl]
	  [-m minttl] [-O length] [-P proxy_username] [-p source_port]
	  [-q seconds] [-s source] [-T keyword] [-V rtable] [-W recvlimit] [-w timeout]
	  [-X proxy_protocol] [-x proxy_address[:port]] 	  [destination] [port]
```

| 选项 | 说明 |
| --- | --- |
| -v | 产生更详细的输出 |
| -z | 只扫描侦听守护进程，不向它们发送任何数据，不能与-l选项一起使用。 |
| -l \<PORT>| 监听传入的连接，而不是启动到远程主机的连接。侦听的目标和端口可以指定为非可选参数，也可以分别使用选项-s和-p。不能与-x或-z一起使用。此外，使用-w选项指定的任何超时都会被忽略 |
| -w\<S> | 设置连接超时时间，单位是秒。默认没有超时时间 |
| -N | 发送数据 |
| -u | 使用UDP协议 |

### 示例
```shell
# 测试到192.168.10.20的3306端口连通性
nc -zv 192.168.10.20 3306

# 测试到baidu.com的8080端口连通性，并设置超时时间为5秒
nc -vz -w5  baidu.com 8080

# 在特定端口上启动nc监听连接
nc -l 1280

# 在特定端口上启动指定地址的nc监听连接
nc -l 127.0.0.1 1280

# 启动nc监听1280端口，并将接收到的数据写入到nc.out文件
nc -l 1280 > nc.out

# 扫描tcp协议80到90端口,并设置超时时间为2秒
nc -zv -w2 192.168.10.20 80-90
```
