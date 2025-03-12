## qemu-img命令

```sh
# 将disk.local转换成qcow2，并输出到disk.local.qcow2
qemu-img convert -f raw -O qcow2  disk.local disk.local.qcow2
```