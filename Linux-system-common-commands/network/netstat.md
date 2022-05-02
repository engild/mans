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

#### 示例
```shell
# 打印所有（包括未启动的）接口信息，显示数字地址
netstat -ain

# 显示eth0接口的信息
netstat -I=eth0
```
