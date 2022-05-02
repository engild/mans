## systemctl命令

向`systemd`管理器查询或发送控制命令。

### 用法
```
systemctl [OPTIONS...] {COMMAND} ...
```

start NAME...  # 启动一个或多个units

stop NAME...  # 停止一个或多个units

reload NAME...  # 重载一个或多个units

restart NAME...  # 重启一个或多个units

try-restart NAME...  # 如果状态是active，则重启一个或多个units

reload-or-restart NAME...  # 如果可以重载，则重载一个或多个units，否则重启

reload-or-try-restart NAME...  # 如果可以重载，则重载一个或多个units，否则重启状态为active的units

isolate NAME    

kill NAME...          

is-active PATTERN...      

is-failed PATTERN...      

status [PATTERN...|PID...]   

show [PATTERN...|JOB...]    

cat PATTERN...         

set-property NAME ASSIGNMENT...

help PATTERN...|PID...     

reset-failed [PATTERN...]    

list-dependencies [NAME]    

### 示例
~~~shell
# 设置为开机自启,并立即启动
systemctl enable --now NAME...

# 重启network服务
systemctl restart network

# 检查是否为活跃状态，退出状态返回0或1
systemctl is-active NAME...

# 检查是否为失败状态，退出状态返回0或1
systemctl is-failed NAME...

# 检查是否为开机自启状态，退出状态返回0或1
systemctl is-enabled NAME...

# 显示units运行状态
systemctl status [PATTERN...|PID...]  
~~~
