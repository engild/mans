## tree命令
以树状格式列出目录的内容。

### 用法
```
tree [-adfghilnpqrstuvxACDFNS] [-H baseHREF] [-T title ] [-L level [-R]]
        [-P pattern] [-I pattern] [-o filename] [--version] [--help] [--inodes]
        [--device] [--noreport] [--nolinks] [--dirsfirst] [--charset charset]
        [--filelimit #] [<directory list>]
```

| 选项 | 说明
| --- | ---
| -L level | 设置深度级别
|  | 
|  | 

### 示例
```sh
# 以树状格式列出/home目录，并设置深度为1
tree -L 1 /home

```
