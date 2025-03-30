## kubectl rollout命令&
说明：管理一个资源的滚动

有效的资源为：`deployments`、`daemonsets`、`statefulsets`

### 用法
```
kubectl rollout SUBCOMMAND [options]
```

| 子命令 | 说明
| --- | ---
| history   | 显示 `rollout` 历史
| pause     | 标记提供的 resource 为中止状态
| resume    | 继续一个停止的 resource
| status    | 显示 rollout 的状态
| undo      | 撤销上一次的 rollout


### 示例
```shell
# 查看rollout历史
kubectl rollout history deployment/abc

# 查看版本 3 的详情
kubectl rollout history daemonset/abc --revision=3

# 回滚到版本 3
kubectl rollout undo daemonset/abc --to-revision=3
```
