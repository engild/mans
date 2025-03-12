## blkid命令
定位或打印块设备属性


### 用法
```
xxx [选项]
```

| 选项 | 说明
| --- | ---
| -o | 
| -s | 
|  | 

### 示例
```sh
# 只打印UUID的值
blkid -o value -s UUID /dev/normalIOvg/lvmbcc
```
