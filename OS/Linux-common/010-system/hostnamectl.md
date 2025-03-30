## hostnamectl命令&
说明：查询或修改系统主机名。

### 用法
```
hostnamectl [OPTIONS...] COMMAND ...
```

| COMMAND | 说明
| --- | ---
| status                | 显示当前主机名设置
| set-hostname NAME     | 设置主机名
| set-icon-name NAME    | 设置主机图标名
| set-chassis NAME      | 设置主机机箱类型
| set-deployment NAME   | 设置主机部署环境
| set-location NAME     | 设置主机位置


| 选项 | 说明
| --- | ---
| -H --host=[USER@]HOST[:22]    | 在远程主机上操作。这需要远程主机有hostnamectl命令，且版本兼容。
| -M --machine=CONTAINER        | 在本地容器上操作
| --json=pretty|short|off       | 指定json格式输出

### 示例
```sh
# 修改主机名为new_hostname
hostnamectl set-hostname new_hostname

# 查询远程主机的主机名等信息
hostnamectl -H $your_hostname_or_ip:622

```