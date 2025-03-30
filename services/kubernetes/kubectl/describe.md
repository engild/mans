## kubectl describe命令&
说明：显示特定资源或资源组的详细信息


### 用法
```
kubectl describe (-f FILENAME | TYPE [NAME_PREFIX | -l label] | TYPE/NAME) [options]
```

| 选项 | 说明
| --- | ---
| --all-namespaces  | 列出所有命名空间下的对象

### 示例
```sh
# 显示pod名nginx的详细信息
kubectl describe pods/nginx

# 显示所有名字以nginx开头的pod详细信息
kubectl describe pods nginx
```
