```sh
# 临时给eth0网卡配置IP为192.168.10.25，且netmask为255.255.255.0
ifconfig eth0 192.168.10.25 netmask 255.255.255.0


# 临时修改mtu值
ifconfig xgbe0 mtu 2000


```