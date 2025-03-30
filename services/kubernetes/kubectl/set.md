## kubectl set命令
说明：更新应用资源配置

### 用法
```
kubectl set SUBCOMMAND [options]
```

| 子命名 | 说明
| --- | ---
| env               | 更新一个pod的环境变更
| image             | 更新一个pod的镜像
| resources         | 使用pod模板更新对象上的资源requests/limits
| selector          | 在资源上设置选择器
| serviceaccount    | 更新资源的ServiceAccount
| subject           | 更新RoleBinding/ClusterRoleBinding中的User、Group或ServiceAccount


### 示例
```sh
# 设置 deployment 的 nginx 容器镜像为 nginx:1.9.1，busybox容器镜像为 busybox`
kubectl set image deployment/nginx busybox=busybox nginx=nginx:1.9.1
```