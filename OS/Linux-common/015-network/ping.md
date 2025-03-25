## ping命令

发送`ICMP`回送请求到网络主机

`ping`使用`ICMP`协议的强制回送请求数据报从主机或网关引出`ICMP`回送响应。回送请求数据报(`ping`有一个`IP`和`ICMP`报头，后面跟着一个结构`timeval`，然后是任意数量的`pad`字节，用来填充数据包。`ping`可以使用`IPv4`和`IPv6`。通过指定`-4`或`-6`可以显式地仅使用其中之一。`ping`还可以发送`IPv6`节点信息查询(`RFC4620`)。可能不允许中间跳转，因为`IPv6`源路由已被弃用(`RFC5095`)

### 用法
```
Usage: ping [-aAbBdDfhLnOqrRUvV64] [-c count] [-i interval] [-I interface] [-m mark] [-M pmtudisc_option] [-l preload] [-p pattern] [-Q tos] [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp_option] [-w deadline] [-W timeout] [hop1 ...] destination

Usage: ping -6 [-aAbBdDfhLnOqrRUvV] [-c count] [-i interval] [-I interface] [-l preload] [-m mark] [-M pmtudisc_option] [-N nodeinfo_option] [-p pattern] [-Q tclass] [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp_option] [-w deadline] [-W timeout] destination

destination表示目标主机，可写IP或者主机名
```
### OPTIONS

-4  # 只使用IPV4地址

-6  # 只使用IPV6地址

-c  # 指定ping几次后停止，如：-c4

-w  # 指定等待时间（以秒为单位），而不管发送或接收了多少包。

-i  # 指定时间间隔（以秒为单位）

-q  # 安静输出，除了启动时和完成时的摘要行外，不显示任何内容。

### 示例
```shell
# ping本地回环网卡地址4次。
ping -c4 127.0.0.1

# 安静输出，等待五秒后退出
ping -qw5 destination
```
