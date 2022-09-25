## iftop命令&

### 用法
```
iftop -h | [-npblNBP] [-i interface] [-f filter code] [-F net/mask] [-G net6/mask6]
```

| 选项 | 说明 |
| --- | --- |
| -n | 不解析主机名 |
| -b | 不展示流量条形图 |
| -B | 以字节为单位显示带宽，默认是以bit显示的 |
| -i interface | 指定监听的网卡名 |
| -P | 显示端口和主机 |
| -m limit | 限制显示带宽的上限，例如：100m |
| -p |  |
| -o 2s | 按第一列排序(平均2s流量) |
| -o 10s | 按第二列排序(平均10s流量)（默认值） |
| -o 40s | 按第三列排序(平均40s流量) |
| -o source | 按源地址排序 |
| -o destination | 按目标地址排序 |
| -F net/mask | 显示IPV4的流量 |
| -G net6/mask6 | 显示IPV6的流量 |
| -t | 使用无ncurses文本界面，多用于结合-s -L选项使用 |
| -s num | 在数秒后打印一个文本输出，然后退出 |
| -L num | 限制每次输出时的行数 |

另外，进入交互模式后还可以按快捷键更改显示方式，注意大小写
| 按键 | 说明 |
| --- | --- |
| General |
| P | pause display |
| h | 显示/隐藏帮助 |
| b | toggle bar graph display |
| B | cycle bar graph average |
| T | toggle cumulative line totals |
| j/k | scroll display |
| f | edit filter code |
| l | set screen filter |
| L | lin/log scales |
| ! | shell command |
| q | quit |
| Host display |
| n | toggle DNS host resolution |
| s | 显示/隐藏源host信息 |
| d | toggle show destination host  |
| t | cycle line display mode |
| Port display |
| N | toggle service resolution |
| S | toggle show source port |
| D | toggle show destination port |
| p | toggle port display |
| Sorting |
| 1/2/3 | sort by 1st/2nd/3rd column |
| < | sort by source name |
| > | sort by dest name |
| o | freeze current order |

```
TX：发送   cum：运行iftop到目前时间的总计   peak：流量峰值   rates：分别表示过去 2s 10s 40s 的平均流量
RX：接收
TOTAL：总计
```

### 示例
```sh
# 以字节为单位显示带宽
iftop -B

# -t -s选项结合，实现输出一次结果到一个文本中
iftop -ts 1 -L 10 > iftop.out
```
