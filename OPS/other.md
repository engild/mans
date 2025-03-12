## 扫描新增磁盘
```sh
for i in `ls /sys/class/scsi_host` ; do echo "- - -" > /sys/class/scsi_host/$i/scan ; done
echo 1  >/sys/bus/pci/slots/69/power
lspci -s 65:00.0 -v |grep -i slot
```

## 将命令输出结果丢弃
ls >/dev/null 2>&1

## 单引号中使用变量
echo 'hello "'${var_name}'"'

## shell设置默认变量
name=${name:-"default value"}
name=${name:="default value"}



## 单引号中调用变量
for i in `cat host`; do curl -s IP/InstanceService -d '{"value1": true, "read_deleted": true, "host": "'${i}'"}' ; done


##  创建多个文件
```sh
touch file{1..5}.txt
ls
# file1.txt  file2.txt  file3.txt  file4.txt  file5.txt
```

## 快速备份
```sh
cp file{,.bak}
ls
# file file.bak
```