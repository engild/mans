## less命令



### 用法
```
xxx [选项]
```

| 选项 | 说明
| --- | ---
| -i | 忽略大小写
| -N | 显示行号
| -S | 不换行显示



### 交互模式用的用法
```sh
# 仅显示匹配的行
&pattern

# 仅显示不匹配的行
&!pattern

# 按m设置标记。将当前位置标记为a
ma

# 按单引号跳转到指定标记，跳转到a标记处
'a
```
