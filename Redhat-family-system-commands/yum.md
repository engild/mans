## yum命令
### 用法
```
yum [options] [command] [package ...]
```
-y   # 自动回答yes
--downloadonly   # 不会真正的安装或更新，仅下载包和依赖的包
--downloaddir=PATH   # 指定下载目录
2.1.1.3.COMMAND
install package1 [package2] [...]	安装软件包
update [package1] [package2] [...]	更新软件包
provides	
remove	移除软件包
repolist [all|enabled|disabled]	
clean [ packages | metadata | expire-cache | rpmdb | plugins | all ]
packages：包
metadata：元数据
all：所有
	清除缓存数据。

makecache	生成元数据缓存
	
	
### 示例
```shell
# 下载packages到/root，不会真正的安装
yum install --downloadonly --downloaddir=/root packages
yum reinstall --downloadonly --downloaddir=/root packages

# 清除所有缓存
yum clean all

# 显示配置的软件存储库
yum repolist
```
