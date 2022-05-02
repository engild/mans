## ss命令&

另一个用于研究套接字的实用程序，类似`netstat`。

### 用法
```
ss [options] [ FILTER ]
```

### options

-n  不去尝试解析服务名称

-p  显示产生进程的用户、进程号（pid）、进程所打开的文件数（fd）。

-t  显示tcp的套接字

-u  显示udp的套接字

-l  只显示LISTEN（监听）状态的套接字。默认情况只显示ESTAB（连接）状态的套接字。

-a  同时显示监听和未监听(对于TCP来说，意味着已经建立连接)的套接字。如果同时使用了-l，-l会失效。

-H  不显示标题行

### FILTER

### 示例
```shell
ss -lntup

ss -ntup | grep 80
```
