## journalctl命令

### 用法	

| 选项 | 说明                                                 |
| ---- | ---------------------------------------------------- |
| -x   | 在可能的地方添加消息解释                             |
| -u   | 显示指定unit的日志                                   |
| -e   | 直接跳到末尾                                         |
| -S   | 显示不超过指定日期的条目，-S 5m表示显示5分钟内的日志 |
| -f   | 跟踪日志输入，类似tail -f                            |
|      |                                                      |

### 示例

~~~shell
journalctl -xe -u network
~~~