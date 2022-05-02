## groupadd命令&

创建新组

### 用法

```
groupadd [options] GROUP
```

| 选项 | 说明                 |
| ---- | -------------------- |
| -g   | 指定新组的ID         |
| -f   | 即使组已存在也不报错 |
### 示例

```shell
# 创建一个组，名为test_group，并设置组ID为600
groupadd -g 600 test_group
```
