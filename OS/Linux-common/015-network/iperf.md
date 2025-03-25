## iperf命令
iperf是一个网络性能测试工具，主要用于测量TCP和UDP带宽性能。它提供了丰富的命令行选项，允许用户进行各种网络性能测试。


### 用法
```
xxx [选项]
```

| 选项 | 说明
| --- | ---
| -t, --time                | 侦听新连接和接收流量的时间(以秒为单位)(默认未设置)
| -p, --port                | 指定服务端要监听或者客户端要连接的端口
| -f, --format [kmgKMG]     | 指定报告格式 <br>k == Kbits, K == KBytes<br>m == Mbits, M == MBytes<br>g == Gbits, G == GBytes
| -i, --interval            | 指定报告间隔
| -D, --daemon              | 将服务器作为守护进程运行

客户端与服务器端选项：

-s：以服务器模式运行iperf，监听指定的端口。
-c host：以客户端模式运行iperf，连接到指定的主机。
设置测试参数：

-t seconds：设置测试的时长，单位为秒。
-l bytes：设置发送的数据包大小，单位为字节。
-u：使用UDP协议进行测试。
-P threads：设置多线程模式，用于同时测试多个连接。

`-w window_size`：设置tcp窗口大小。
`-n packets`：设置发送的数据包数量。
`-f format：设置输出格式，如k、M、G`等。
-i seconds：设置报告间隔时间，单位为秒。
`-b bandwidth`：设置UDP发送带宽，单位为bit/s。
获取帮助：

--help或-h：显示帮助信息。
`--version`或-v：显示版本信息。
使用iperf时，可以通过组合这些选项来执行特定的网络性能测试。例如，要测试与远程主机的TCP带宽，可以使用命令iperf -c target_host -t 60 -l 10M，这表示以客户端模式连接到目标主机，进行60秒的测试，并发送10MB的数据包。同样地，要测试UDP带宽，可以使用命令iperf -u -c target_host -t 60 -l 10M -b 10Mbit/s，这表示使用UDP协议进行测试，带宽设置为10Mbps。

### 示例
```sh
# 示例的注释
命令示例
iperf -s -p 7788
iperf -c 10.72.74.251 -p 7788 -t 1024 -i 1 -P 1 -M 1000 -m

```

