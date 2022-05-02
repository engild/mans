# apt命令
### apt使用代理

编辑/etc/apt/apt.conf.d/10proxy
~~~
Acquire::http::Proxy "http://192.168.68.116:1080";
~~~

### 示例

```shell
# 更新可用软件包列表
apt update

# 列出所有已安装的包
apt list --installed

# 安装一个或多个包
apt install ncat iftop

# 重新安装包
apt reinstall nginx

# 升级指定的包
apt-get install --only-upgrade policykit-1

# 移除包
apt remove mysql

# 卸载所有自动安装且不再使用的软件包
apt autoremove

```
