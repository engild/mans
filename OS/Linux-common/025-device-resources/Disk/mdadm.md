mdadm命令
mdadm --detail /dev/md0
mdadm -D /dev/md0


cat /proc/mdstat


mdadm -S /dev/md127
mdadm --misc --zero-superblock /dev/sdg1
mdadm --misc --zero-superblock /dev/sdh1

sgdisk -Z /dev/sd

rm -f /etc/mdadm.conf
/etc/mdadm/mdadm.conf

parted -s /dev/sdi mklabel gpt
parted -s /dev/sdi mkpart primary ext4 2048s 100%
mke2fs -F -t ext4 -b 4096 -i 8192 -I 256 -m0 /dev/sde1


sgdisk -Z /dev/sd