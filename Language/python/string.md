
### 保证字符串是5位，不足时在左侧用 0 补齐
```python
s = "123"
s = s.zfill(5)
```

### 用指定字符将列表中的元素拼接成字符串
```python
list1 = ["a", "b", "c", "d"]
str1 = '--'.join(list1)
print(str1)
```