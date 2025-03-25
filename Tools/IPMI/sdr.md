## sdr命令
打印传感器数据
包括cpu、内存、磁盘温度，风扇转速等信息

### 用法
```
xxx [选项]
```

| 选项 | 说明
| --- | ---
|  | 
|  | 
|  | 


SYS_Fan1_Speed_F    转速
SYS_Fan1_Present    转速百分比



### 示例
```sh
# 简单打印
sdr

# 超详细打印
ipmitool -v sdr | grep -A 20 0xe8

# 获取指定传感器的信息
sdr get CPU1_PVPP1

# 按照Sensor类型读取（sdr type）sensor类型可以通过sdr type list命令来列举：
sdr type list

# 读取风扇相关的传感器数据
sdr type fan

# 读取电压相关的传感器数据
sdr type Voltage

# 读取温度相关的传感器数据
sdr type Temperature
# 比list额外显示编号?
sdr elist
```