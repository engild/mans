## readlink命令
输出符号链接值或权威文件名

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
# 查看文件/home/filename链接到哪里了
readlink /home/filename

# 查看目录/home/dir_name链接到哪里了，注意，看目录时一定不要带最后的 / ，用rm删除时也一定不能带 / ，否则后删除链接的源文件中所有文件！！！
readlink /home/dir_name

# 用-f选项时好像可以加 /
readlink -f /home/dir_name/


```