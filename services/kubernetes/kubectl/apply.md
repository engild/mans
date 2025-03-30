## kubectl apply命令
说明：将配置应用于资源。

### 用法
```
kubectl apply -f FILENAME [options]
```

| 选项 | 说明
| --- | ---
| -f, --filename= | 指定配置文件
|  | 
|  | 

### 示例
```sh
# 通过文件应用配置到资源上
kubectl apply -f nginx-pod.yaml

```