## nvidia-smi命令
说明：nvidia系统管理接口

### 用法
```
nvidia-smi [OPTION1 [ARG1]] [OPTION2 [ARG2]] ...
```

| 选项 | 说明
| --- | ---
| -L,   --list-gpus             | 显示已连接到系统的GPU列表
| -B,   --list-excluded-gpus    | 显示系统中排除的GPU列表
| -q,   --query                 | 显示GPU或Unit信息
| -i,   --id=                   | 指定GPU
| -l,   --loop=                 | 指定刷新间隔N秒
| -lms, --loop-ms=              | 指定刷新间隔N毫秒
| --format=                     | 输出格式



### 示例
```sh
# 显示GPU的详细信息
# 包括硬件规格、驱动版本、显存信息、功耗管理、温度控制、GPU拓扑结构等信息。使用该命令可以了解GPU的硬件配置、驱动版本、显存大小、功耗管理策略、温度控制策略等信息，以及GPU的连接关系、拓扑结构等信息。
nvidia-smi -q


# 显示GPU设备的显存使用情况和GPU的繁忙度。使用该命令可以实时监测GPU的显存使用情况和GPU的繁忙度，并以文本形式输出。
nvidia-smi dmon

# 显示GPU拓扑结构和连接关系，可用于识别GPU间连接的带宽和延迟等信息。使用该命令可以了解GPU设备之间的连接关系和拓扑结构，以及GPU设备之间的带宽和延迟等信息。
nvidia-smi topo -m

# 这个命令用于查看显卡间的NVLink连接状态，可以确定系统中的显卡是否成功互联。
nvidia-smi nvlink –status
```