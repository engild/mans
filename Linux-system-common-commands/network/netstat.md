## netstat命令

打印网络连接、路由表、接口统计数据、伪装连接和多播成员关系

### 用法

netstat  [address_family_options]  [--tcp|-t]  [--udp|-u]  [--udplite|-U] [--sctp|-S] [--raw|-w] [--listening|-l] [--all|-a] [--numeric|-n] [--numeric-hosts] [--numeric-ports] [--numeric-users] [--symbolic|-N] [--extend|-e[--extend|-e]] [--timers|-o] [--program|-p]  [--verbose|-v]  [--continuous|-c]  [--wide|-W] [delay]

netstat {--route|-r} [address_family_options] [--extend|-e[--extend|-e]] [--verbose|-v] [--numeric|-n] [--numeric-hosts] [--numeric-ports] [--numeric-users]  [--continuous|-c] [delay]

netstat {--interfaces|-I|-i} [--all|-a] [--extend|-e] [--verbose|-v]  [--program|-p]  [--numeric|-n]  [--numeric-hosts]  [--numeric-ports]  [--numeric-users]    [--continuous|-c] [delay]

netstat {--groups|-g} [--numeric|-n] [--numeric-hosts] [--numeric-ports] [--numeric-users] [--continuous|-c] [delay]

netstat {--masquerade|-M} [--extend|-e] [--numeric|-n] [--numeric-hosts] [--numeric-ports] [--numeric-users] [--continuous|-c] [delay]

netstat {--statistics|-s} [--tcp|-t] [--udp|-u] [--udplite|-U] [--sctp|-S] [--raw|-w] [delay]

netstat {--version|-V}

netstat {--help|-h}

address_family_options:

 [-4|--inet]  [-6|--inet6]  [--protocol={inet,inet6,unix,ipx,ax25,netrom,ddp,  ...  }  ]  [--unix|-x]  [--inet|--ip|--tcpip] [--ax25] [--x25] [--rose] [--ash]    [--ipx] [--netrom] [--ddp|--appletalk] [--econet|--ec]

### 选项

-a  显示所有状态的套接字。使用—interfaces或-i选项，显示未启动的接口

-n  显示数字地址，而不是试图确定符号主机、端口或用户名

--interfaces=iface , -I=iface , -I  # 显示所有网络接口或指定iface的表。

### Flags说明
U Up:           路由处于活动状态。
H Host:         路由目标是单个主机。
G Gateway:      所有发到目的地的网络传到这一远程系统上， 并由它决定最后发到哪里。
S Static:       这个路由是手工配置的，不是由系统自动生成的。
C Clone:        生成一个新的路由， 通过这个路由我们可以连接上这些机子。 这种类型的路由通常用于本地网络。
W WasCloned:    指明一个路由——它是基于本地区域网络 (克隆) 路由自动配置的。
L Link:         路由涉及到了以太网硬件。

#### 示例
```shell
# 打印所有（包括未启动的）接口信息，显示数字地址
netstat -ain

# 显示eth0接口的信息
netstat -I=eth0
```
