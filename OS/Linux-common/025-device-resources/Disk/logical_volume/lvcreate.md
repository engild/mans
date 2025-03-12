## lvcreate命令

创建一个逻辑卷

lvcreate在VG中创建一个新的LV。对于标准lv，这需要从VG的空闲物理区段中分配逻辑区段。如果没有足够的空闲空间，可以使用其他pv扩展VG (vgextend(8))，或者减少或删除现有的lv (lvremove(8)、lvreduce(8))。

要控制一个新LV将使用哪些pv，可以在命令行末尾指定一个或多个pv作为位置参数。lvcreate将只从指定的pv分配物理区段。

lvcreate还可以创建现有lv的快照，例如用于备份。新快照LV中的数据表示创建快照时原始LV的内容。

RAID LV可以通过在创建LV时指定LV类型来创建(参见lvmraid(7))。不同的RAID级别需要在VG中提供不同数量的惟一pv进行分配。


Create a linear LV.
  lvcreate -L|--size Size[m|UNIT] VG
        [ -l|--extents Number[PERCENT] ]
        [    --type linear ]
        [ COMMON_OPTIONS ]
        [ PV ... ]

### 示例
```sh

