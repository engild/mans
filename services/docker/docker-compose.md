## docker-compose命令

### 用法
```
docker-compose [-f <arg>...] [options] [COMMAND] [ARGS...]
```

| COMMAND | 说明 |
| ------- | ----------------------------------------------- |
| up      |                                                 |
| down    | 停止并移除containers, networks, images和volumes |
| start   | 启动服务                                        |
| restart | 重启服务                                        |
| stop    | 停止服务                                        |
| ps      | 列出containers                                  |
| rm      | 移除停止的容器                                  |
| images  | 列出images                                      |

### 示例
```shell
docker-compose down

docker-compose up -d
```
