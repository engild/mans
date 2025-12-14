## docker load命令
说明：从tar存档或STDIN加载镜像。

注：通过export导出的镜像，不可以使用load加载，应该用import导入。

### 用法
```
docker load [Options]
```

| 选项 | 说明
| --- | ---
| -i    | 指定从tar存档文件(而不是STDIN)读取
| -q    | 不输出导入过程

### 示例
```shell
# 从/root/test.tar导入镜像，不显示导入过程。
docker load -qi /root/test.tar
```
