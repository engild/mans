## vgcreate命令

创建卷组

vgcreate在块设备上创建一个新的VG。如果设备以前没有使用pvcreate(8)初始化为pv，那么vgcreate将初始化它们，使它们成为pv。用于初始化设备的pvcreate选项也可以在vgcreate中使用。
