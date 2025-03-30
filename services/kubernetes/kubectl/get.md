## kubectl get命令&
说明：显示一个或多个资源
可以通过执行 `kubectl api-resources` 命令来获取有哪些类似的资源可以查询

### 用法
```
kubectl get
[(-o|--output=)json|yaml|wide|custom-columns=...|custom-columns-file=...|go-template=...|go-template-file=...|jsonpath=...|jsonpath-file=...]
(TYPE[.VERSION][.GROUP] [NAME | -l label] | TYPE[.VERSION][.GROUP]/NAME ...) [flags] [options]
```

| 选项 | 说明
| ---- | ---
| --all-namespaces  | 指定所有命名空间
| -n                | 指定命名空间。可以通 `kubectl get namespaces` 查看命名空间
| -o, --output=''   | 指定输出格式。可选为：`json\|yaml\|wide\|custom-columns=...\|custom-columns-file=...\|go-template=...\|go-template-file=...\|jsonpath=...\|jsonpath-file=...`
| --show-labels     | 显示资源的标签


### 示例
```sh
# 以ps输出格式列出所有pod，并提供更多信息(如节点名称)。
kubectl get pods -o wide

# 列出所有的命名空间
kubectl get namespaces

# 列出指定的副本控制器
kubectl get replicationcontroller web
kubectl get replicationcontroller/web

# 同时列出多种资源
kubectl get rc,services
kubectl get rc/web service/frontend pods/web-pod-13je7

# 获取指定资源信息，只展示指定字段
kubectl get pod test-pod -o custom-columns=ONTAINER:.spec.containers[0].name,IMAGE:.spec.containers[0].image

# 通过json格式展示指定资源信息
kubectl get pod web-pod-13je7 -o json

# 获取指定资源信息，只展示特定的值
kubectl get pod/web-pod-13je7 -o template --template={{.status.phase}}
```
