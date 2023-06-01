```sh
# 结合tail命令，查看一个或多个文件的增长速度
tail -f file01 file02 | dd of=/dev/null status=progress
```