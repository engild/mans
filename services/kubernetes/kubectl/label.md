## kubectl label命令

### 示例

~~~shell
# 删除一个标签。只需在标签名后面跟一个减号
kubectl label nodes 节点名 标签名-

# 修改一个标签的值
kubectl label nodes --overwrite 节点名 标签名=新值
~~~