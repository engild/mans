## vgremove命令
移除卷组

### 用法
```
vgremove
        [-d|--debug]
        [-f|--force]
        [-h|--help]
        [--noudevsync]
        [-t|--test]
        [-v|--verbose]
        [--version]
        VolumeGroupName [VolumeGroupName...]
```

| 选项 | 说明 |
| --- | --- |
|  |  |
|  |  |
|  |  |

### 示例
```sh
# 移除多个卷组
vgremove normalIOvg1 normalIOvg2

# 移除normalIOvg0 到 normalIOvg10
vgremove normalIOvg{0..10}

```
