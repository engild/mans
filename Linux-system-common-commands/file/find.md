## find命令

在目录中搜索文件

### 用法

find [-H] [-L] [-P] [-D debugopts] [-Olevel] [path...] [expression]

### expression（表达式）

| 限制                                          | 说明                                                         |
| --------------------------------------------- | ------------------------------------------------------------ |
| -maxdepth                                     | 最大查找深度                                                 |
| -mindepth                                     | 最小查找深度                                                 |
|                                               |                                                              |
| 条件                                          |                                                              |
| -type  指定文件类型                           | f  普通文件，d  目录，b  块设备文件，l  符号链接文件，s  socket文件，c  字符设备文件，p  管道文件 |
| -name  按文件名查找-iname  忽略文件名的大小写 | -name *.log  查找文件名以.log为结尾的-name *test*  查找文件名包含test的 |
| -empty                                        | 查找空文件或目录                                             |
| -mtime-ctime-atime                            | 分别为修改时间、创建时间和访问时间，以天为单位。例如：+5表示5天之前，-5 表示5天之内-100 +50表示查找100天以内50天之前的文件-atime 5表示从上次访问到现在相隔大于5天而小于6天的 |
| -mmin-cmin-amin                               | 与time类似，不同的是min以分钟为单位                          |
| -gid                                          | 指定文件的gid                                                |
| -group                                        | 指定文件的属组                                               |
| -nogroup                                      | 查找没有属组的文件                                           |
| -uid                                          | 指定文件的uid                                                |
| -user                                         | 指定文件的属主                                               |
| -nouser                                       | 查找没有属主的文件                                           |
| -anewer                                       | 查找比某一个文件新的                                         |
| -size                                         | 以文件大小为条件，单位可以是bcwkMG，+1G表示大于1G的文件，-10M表示小于10M的文件 |
|                                               |                                                              |
| 动作                                          |                                                              |
| -delete                                       | 将查找出来的文件删除                                         |
| -exec COMMAND \;-exec COMMAND {} \;           | 查到内容时要执行的命令，每查到一个内容都会执行一遍。{}表示查到的内容 |


```sh
# 查找修改时间是100天前的
find /home/your-path -mtime +100

# 查找并删除，访问时间是30天前，大小大于500M，类型是文件的，名字是test.log结尾的
find /home/logs -name "*test.log" -type f -size +500M -atime +30 -exec rm {} \;

```