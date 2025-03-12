## sensor命令
打印传感器的详细信息
和sdr命令极为相似

### 用法
```
xxx [选项]
```

| 选项 | 说明
| --- | ---
|  | 
|  | 
|  | 

### 示例
```sh
# 获取所有传感器的信息
sensor   # 等同于sensor list

# 获取指定传感器的信息，例如：获取风扇总功耗
sensor get Fan_Total_Power
# 再过滤"Sensor Reading"可以得到当前值
sensor get Fan_Total_Power | grep Reading

sensor get "CPU1 Temp"

```
