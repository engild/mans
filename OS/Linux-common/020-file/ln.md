## ln命令
这里写命令的简单说明

### 用法
```
Usage: ln [OPTION]... [-T] TARGET LINK_NAME
  or:  ln [OPTION]... TARGET
  or:  ln [OPTION]... TARGET... DIRECTORY
  or:  ln [OPTION]... -t DIRECTORY TARGET...
In the 1st form, create a link to TARGET with the name LINK_NAME.
In the 2nd form, create a link to TARGET in the current directory.
In the 3rd and 4th forms, create links to each TARGET in DIRECTORY.
Create hard links by default, symbolic links with --symbolic.
By default, each destination (name of new link) should not already exist.
When creating hard links, each TARGET must exist.  Symbolic links
can hold arbitrary text; if later resolved, a relative link is
interpreted in relation to its parent directory.
```

| 选项 | 说明
| --- | ---
|  | 
|  | 
|  | 

### 示例
```sh
# 创建软链接文件/home/yufei，链接位置是目录/home/nvme1n1/yufei/
ln -s /home/nvme1n1/yufei/ /home/yufei

```
