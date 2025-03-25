
### 定义一个函数
```python
def function_name():
    pass


```

#### 保留两位小数
```python
f = round(3.14159, 2)
print(f)

3.14

```

#### 获取类中所有函数并执行
```python
func_names = [attr for attr in dir(Class_name) if callable(getattr(Class_name, attr))]
func_names = [attr for attr in dir(Class_name) if not attr.startswith("__")]
print("类中的所有函数名称：", func_names)
for name in func_names:
    getattr(machine_info, name)()
```