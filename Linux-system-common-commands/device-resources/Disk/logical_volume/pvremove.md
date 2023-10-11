## pvremove命令
移除物理卷

### 用法
```
pvremove 
        [-d|--debug]
        [-f[f]|--force [--force]] 
        [-h|-?|--help] 
        [-t|--test] 
        [-v|--verbose] 
        [-y|--yes]
        [--version] 
        PhysicalVolume [PhysicalVolume...]
```

| 选项 | 说明 |
| --- | --- |
|  |  |
|  |  |
|  |  |

### 示例
```sh
# 示例的注释
pvremove /dev/sdb

# 移除/dev/sdb /dev/sdc ... /dev/sdl物理卷
pvremove /dev/sd{b..l}

```
