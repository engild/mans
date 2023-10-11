## fping

### 用法
```
fping [options] [targets...]
```

| 选项 | 说明 |
| --- | --- |
| -a, --alive | 显示alive的目标 |
| -u, --unreach | 显示unreachable的目标 |
| -f, --file=FILE | 从文件中读取目标列表 |
| -r, --retry=N | 重试次数，默认为3次 |
| -t, --timeout=MSEC | 单个目标初始超时（默认值：500毫秒，使用-l/-c/-C除外，其中-p周期最长可达2000毫秒） |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

### 示例
```sh
# ping hostlist.txt文件中的目标，仅显示不通的目标
fping -u -f hostlist.txt

```
