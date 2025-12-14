## terraform命令&
说明：terraform工具相关命令

terraform是一个开源的基础设施即代码工具，用于构建、更改和版本化云和本地基础设施。

### 用法
```
terraform [全局] <子命令> [参数]

子命令的用法见同级目录下的手册
```

| 全局选项 | 说明
| --- | ---
| -version  | 显示版本信息 | 
| -help     | 显示帮助信息 | 
| -chdir    | 切换工作目录 | 

### 示例
```sh
# 查看子命令的帮助信息
terraform -help init

# 命令自动补全
terraform -install-autocomplete
```
