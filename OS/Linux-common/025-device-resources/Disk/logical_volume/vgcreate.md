## vgcreate命令
创建一个卷组

vgcreate在块设备上创建一个新的VG。如果设备以前没有使用pvcreate(8)初始化为pv，那么vgcreate将初始化它们，使它们成为pv。用于初始化设备的pvcreate选项也可以在vgcreate中使用。

### 用法
```
vgcreate
        [-A|--autobackup {y|n}] 
        [--addtag Tag] 
        [--alloc AllocationPolicy] 
        [-c|--clustered {y|n}] 
        [-d|--debug]
        [-h|--help]
        [-l|--maxlogicalvolumes MaxLogicalVolumes]
        [-M|--metadatatype 1|2] 
        [--[vg]metadatacopies #copies] 
        [-p|--maxphysicalvolumes MaxPhysicalVolumes] 
        [-s|--physicalextentsize PhysicalExtentSize[bBsSkKmMgGtTpPeE]] 
        [-t|--test] 
        [-v|--verbose]
        [--version] 
        [ PHYSICAL DEVICE OPTIONS ] 
        VolumeGroupName PhysicalDevicePath [PhysicalDevicePath...]
```

| 选项 | 说明 |
| --- | --- |
|  |  |
|  |  |
|  |  |

### 示例
```sh
# 用/dev/sdc /dev/sdd两个PV创建一个VG，名为vg1
vgcreate vg1 /dev/sdc /dev/sdd

```
