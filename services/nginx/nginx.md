## nginx命令
说明：nginx服务相关命令

### 用法
```
nginx [-?hvVtTq] [-s signal] [-p prefix] [-e filename] [-c filename] [-g directives]
```

| 选项 | 说明
| --- | ---
| -h            | 显示帮助信息并退出
| -v            | 显示版本信息并退出
| -V            | 显示版本信息、编译信息和配置选项并退出
| -t            | 测试配置文件是否正确
| -T            | 测试配置文件是否正确，并显示详细信息
| -q            | 不显示任何信息
| -s signal     | 发送信号给主进程
| -p prefix     | 指定配置文件的路径
| -e filename   | 指定配置文件的名称
| -c filename   | 指定配置文件的路径和名称
| -g directives | 设置全局配置选项


| 信号 | 说明
| --- | ---
| stop          | 快速关闭
| quit          | 等待请求处理完毕后关闭
| reload        | 重新加载配置文件
| reopen        | 重新打开日志文件



### 示例
```sh
# 示例的注释
命令示例

```
