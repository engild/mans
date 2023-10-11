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

## shell位置参数
$1 $2 ${12} $* $@ $#

## 单引号中调用变量
for i in `cat uuid_list`; do echo -n "$i "; curl -s 10.210.137.18:9966/InstanceService/instance_get_by_uuid -d '{"is_admin": true, "read_deleted": true, "uuid": "'${i}'"}' | python3 -m json.tool | grep -A1 open_ipv6 | tail -1 ; done


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