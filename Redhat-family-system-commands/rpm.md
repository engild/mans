## rpm命令
rpm包管理器
### 用法
```
常用选项：
-v   # 显示详细信息
-vv   # 更加详细的显示
2.1.1.1.查询用法
rpm {-q|--query} [select-options] [query-options]
2.1.1.1.1.select-options
-a   # 查询所有已安装的包
-f FILE   # 查询文件属于哪个包

2.1.1.1.2.query-options
-i   # 显示包信息
-l   # 显示这个包的文档
-s   # 显示包中文件的状态
-l   # 列出已安装的包都产生了哪些文件


2.1.1.2.验证用法
rpm {-V|--verify} [select-options] [verify-options]
2.1.1.3.安装用法
rpm {-i|--install} [install-options] PACKAGE_FILE ...
2.1.1.3.1.install-options


2.1.1.4.更新用法
rpm {-U|--upgrade} [install-options] PACKAGE_FILE ...
rpm {-F|--freshen} [install-options] PACKAGE_FILE ...
2.1.1.5.移除用法
rpm {-e|--erase} [--allmatches] [--justdb] [--nodeps] [--noscripts] [--notriggers] [--test] PACKAGE_NAME ...
2.1.1.5.1.options
--test   # 不会真正删除，只是去尝试，配合-vv选项去调试。
2.1.1.6.其他
   MISCELLANEOUS:
       rpm {--querytags|--showrc}

       rpm {--setperms|--setugids} PACKAGE_NAME ...

   select-options
        [PACKAGE_NAME] [-a,--all] [-f,--file FILE]
        [-g,--group GROUP] {-p,--package PACKAGE_FILE]
        [--hdrid SHA1] [--pkgid MD5] [--tid TID]
        [--querybynumber HDRNUM] [--triggeredby PACKAGE_NAME]
        [--whatprovides CAPABILITY] [--whatrequires CAPABILITY]

   query-options
        [--changelog] [-c,--configfiles] [--conflicts]
        [-d,--docfiles] [--dump] [--filesbypkg] [-i,--info]
        [--last] [-l,--list] [--obsoletes] [--provides]
        [--qf,--queryformat QUERYFMT] [-R,--requires]
        [--scripts] [-s,--state] [--triggers,--triggerscripts]

   verify-options
        [--nodeps] [--nofiles] [--noscripts]
        [--nodigest] [--nosignature]
        [--nolinkto] [--nofiledigest] [--nosize] [--nouser]
        [--nogroup] [--nomtime] [--nomode] [--nordev]
        [--nocaps] [--noconfig] [--noghost]

   install-options
        [--allfiles] [--badreloc] [--excludepath OLDPATH]
        [--excludedocs] [--force] [-h,--hash]
        [--ignoresize] [--ignorearch] [--ignoreos]
        [--includedocs] [--justdb] [--nocollections]
        [--nodeps] [--nodigest] [--nosignature] [--noplugins]
        [--noorder] [--noscripts] [--notriggers]
        [--oldpackage] [--percent] [--prefix NEWPATH]
        [--relocate OLDPATH=NEWPATH]
        [--replacefiles] [--replacepkgs]
        [--test]
```
