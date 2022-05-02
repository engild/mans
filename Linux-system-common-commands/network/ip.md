## ip命令

### 用法
`ip`很多子命令可以被缩写，比如`ip address`可以被缩写为`ip addr`或者`ip a`，具体如下：

| 标准写法          | 缩写形式      |
| ----------------- | ------------- |
| ip address        | ip addr, ip a |
| ip address show   | ip a s        |
| ip address delete |               |
| ip route          | ip r          |
| ip route add      | ip r a        |
| ip route del      | ip r d        |
|                   |               |

### 示例

~~~shell
# 显示所有网卡信息
ip addr

# 显示eth0网卡的信息
ip addr show eth0

# 查看路由信息
ip route

# 添加静态路由，访问192.168.0.0/24通过192.168.0.1
ip route add 192.168.0.0/24 via 192.168.0.1

# 增加默认路由，via 192.168.0.1 是我的默认路由器
ip route add default via 192.168.0.1 dev eth0

# 删除路由
ip route add 192.168.1.1 dev 192.168.0.1
add 增加路由
del 删除路由
via 网关出口 IP地址
dev 网关出口 物理设备名

# 删除eth0网卡上“192.168.0.1”这个IP
ip addr del 192.168.0.1 dev eth0
~~~

保存路由设置，使其在网络重启后任然有效

在/etc/sysconfig/network-script/目录下创建名为route- eth0的文件

~~~
vi /etc/sysconfig/network-script/route-eth0
在此文件添加如下格式的内容

192.168.1.0/24 via 192.168.0.1
~~~
