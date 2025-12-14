## docker push命令
说明：推送镜像

将镜像推到注册表`docker hub` 或者私有 `registry`

### 用法
```
docker push [Options] NAME[:TAG]
```

| 选项 | 说明 |
| --- | --- |
| --disable-content-trust | 跳过镜像签名（默认为真），用不到 |

### 示例
```shell
# 推送指定镜像
docker push yudeyu/nginx:1.17.10
```
