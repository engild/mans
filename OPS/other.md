## 扫描新增磁盘
for i in `ls /sys/class/scsi_host` ; do echo "- - -" > /sys/class/scsi_host/$i/scan ; done

## 将命令输出结果丢弃
ls >/dev/null 2>&1