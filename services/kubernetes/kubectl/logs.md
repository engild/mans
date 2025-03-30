## kubectl logs命令&
说明：打印pod或指定资源中的容器的日志

### 用法
```
kubectl logs [-f] [-p] (POD | TYPE/NAME) [-c CONTAINER] [options]
```

| 选项 | 说明
| --- | ---
| -p                    | 容器终止前的日志
| -c CONTAINER          | 当一个 `pod` 中有多个容器时，需要加 `-c` 选项来指定查看 `pod` 中哪个容器的日志。`-c init` 可以查看初始化容器日志
| --all-containers=true | 查看 `pod` 中所有容器的日志
| --tail N              | 查看最后 N 行日志
| -f                    | 跟踪日志输出，类似于 `tail` 命令的 `-f` 选项
| --since=1h            | 查看最近1小时的日志,也可以写 `10s` ，`5m` 等
| -l app=nginx          | 查看标签 `app` 为 `nginx` 的日志
| --timestamps          | 输出日志时显示时间戳


### 示例
```sh
# 返回 ruby 这个 pod 中的 web-1 容器终止前的日志
kubectl logs -p -c ruby web-1

# 返回pod名为nginx中所有容器的日志
kubectl logs nginx --all-containers=true

# 从名为hello的job的第一个容器返回日志
kubectl logs job/hello

# 从名为nginx的deployment中返回容器名为nginx-1的日志
kubectl logs deployment/nginx -c nginx-1
```
