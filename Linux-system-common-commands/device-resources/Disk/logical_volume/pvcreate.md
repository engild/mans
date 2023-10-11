## pvcreate命令
初始化LVM使用的物理卷

### 用法
```
pvcreate 
        [--norestorefile]
        [--restorefile file]
        [-d|--debug]
        [-f[f]|--force [--force]] 
        [-h|-?|--help] 
        [--labelsector sector] 
        [-M|--metadatatype 1|2]
        [--pvmetadatacopies #copies]
        [--metadatasize MetadataSize[bBsSkKmMgGtTpPeE]]
        [--dataalignment Alignment[bBsSkKmMgGtTpPeE]]
        [--dataalignmentoffset AlignmentOffset[bBsSkKmMgGtTpPeE]]
        [--setphysicalvolumesize PhysicalVolumeSize[bBsSkKmMgGtTpPeE]
        [-t|--test] 
        [-u|--uuid uuid] 
        [-v|--verbose] 
        [-y|--yes]
        [-Z|--zero {y|n}]
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
# 创建物理卷
pvcreate /dev/sdb

# 创建/dev/sdb /dev/sdc ... /dev/sdl物理卷
pvcreate /dev/sd{b..l}
```
