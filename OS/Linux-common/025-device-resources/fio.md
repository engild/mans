fio命令


```sh
# 4K随机读
fio -filename=/home/disk12/rand_read_16K.txt -direct=1 -iodepth 1 -thread -rw=randread -ioengine=psync -bs=16k -size=100G -numjobs=50 -runtime=120 -group_reporting -name=rand_100read_16k

# 4K顺序读
fio -filename=/home/disk12/sqe_read_16K.txt -direct=1 -iodepth 1 -thread -rw=read -ioengine=psync -bs=16k -size=100G -numjobs=50 -runtime=120 -group_reporting -name=sqe_100read_16k

# 4K随机写
fio -filename=/home/disk12/rand_write_16K.txt -direct=1 -iodepth 1 -thread -rw=randwrite -ioengine=psync -bs=16k -size=100G -numjobs=50 -runtime=120 -group_reporting -name=rand_100write_16k

# 4K顺序写
fio -filename=/home/disk12/sqe_write_16K.txt -direct=1 -iodepth 1 -thread -rw=write -ioengine=psync -bs=16k -size=100G -numjobs=50 -runtime=120 -group_reporting -name=sqe_100write_16k
```