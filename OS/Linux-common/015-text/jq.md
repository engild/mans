## jq命令
这里写命令的简单说明

### 用法
```
jq [options] <jq filter> [file...]
        jq [options] --args <jq filter> [strings...]
        jq [options] --jsonargs <jq filter> [JSON_TEXTS...]
```

| 选项 | 说明
| --- | ---
| -r | 去除输出值的引号
|  | 
|  | 

### 示例
```sh
# 取json文本中key为id的值
| jq '.id'

# 如果host的值是一个列表，用[N]取值
| jq '.host[0].id'

# 遍历
echo '[1,2,3,4]' | jq '.[]'

# instances是个列表，遍历instances，打印每个数据中的id字段
jq '.instances[].id'

# 使用map函数遍历数组，进行处理或转换
echo '[1,2,3,4]' | jq 'map(. * 2)' 

# 如果数据中有hostname，才会读。这种方式不会返回null
jq 'select(has("hostname")) | .hostname'

# 查找一个元素是字典的列表，如果元素的key1的值等于AAA，则显示key2的值
jq '.[] | select(.key1 == "AAA") | .key2'

# 过滤host字段包含AAA
jq '.[] | select(.host | contains("AAA")) | .'

# 展示多个key
jq .key1,.key2
jq '.key1 + "\t" + .key2'

# 打印时数字转成字符串
jq '.key1 + "\t" + (.key2 | tostring)'

# 设置默认值
jq '."value" // 0 as $value | "The value is: " + ($value | tostring)' input.json


```
