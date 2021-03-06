## free命令

显示内存使用相关信息（根据`/proc/meminfo`文件）

### 用法
```
free [options]
```
| 选项 | 说明                                                 |
| ---- | ---------------------------------------------------- |
| -h   | 易读模式输出                                         |
| -b   | 以字节为单位展示                                     |
| -k   | 以千字节为单位                                       |
| -m   | 以兆字节为单位                                       |
| -g   | 以千兆字节为单位                                     |
| -w   | 宽格式输出，在此模式下，缓冲区和缓存在两个分开展示。 |
| -c   | 指定刷新几次，必须配合-s使用。                       |
| -s   | 指定刷新间隔（单位为秒）                             |
| -t   | 在最后一行显示总计                                   |
|      |                                                      |

#### 示例

~~~shell
# 以易读模式输出内存信息
free -h

# 每隔三秒刷新一次结果，共显示5次
free -s3 -c5
~~~
