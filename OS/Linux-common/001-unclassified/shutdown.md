## shutdown命令
关闭系统

### 用法
```
shutdown [OPTIONS...] [TIME] [WALL...]
```

| 选项 | 说明
| --- | ---
| -H --halt     | 停止系统，效果类似ipmitool power soft
| -r --reboot   | 重启机器
| -h            | Equivalent to --poweroff, overridden by --halt
| -P --poweroff | Power-off the machine
| -k            | Don't halt/power-off/reboot, just send warnings
| --no-wall     | Don't send wall message before halt/power-off/reboot
| -c            | Cancel a pending shutdown

### 示例
```sh
# 取消挂起的关机操作
shutdown -c

# 重启服务器
shutdown -r

# 
shutdown -H

shutdown -h


```



centos
# 配置项存在  echo "HandlePowerKey=halt" >> /etc/systemd/logind.conf
# 已开启systemctl status acpid

power soft 最终系统会半关，但是不会完全关掉、断电，智能卡也不会关机。此时power on无法开机，需要执行power reset才能启动

前端执行停止，使用power soft，也是关不掉机，这种也不会掉电，智能网卡也不会关机，开启时检查状态是power on，所以执行了reset


HandlePowerKey=halt   # power soft关不掉
HandlePowerKey=poweroff   # power soft会掉电


# power soft的不掉电
```sh
# 检查HandlePowerKey是否为halt，如果不是则修改为halt
grep "^HandlePowerKey=halt" /etc/systemd/logind.conf

# 确保acpid服务开启，并设置开机自启
systemctl enable --now acpid
```