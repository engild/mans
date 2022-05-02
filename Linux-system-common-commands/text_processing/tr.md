## tr命令

替换、压缩 "和/或" 删除标准输入中的字符 ，写入到标准输出。

### 用法
```
tr [OPTION]... SET1 [SET2]

  -s, --squeeze-repeats   replace each sequence of a repeated character
                            that is listed in the last specified SET,
                            with a single occurrence of that character
  -t, --truncate-set1     first truncate SET1 to length of SET2

SET 是一组字符串，一般都可按照字面含义理解。解析序列如下：

  \NNN	八进制值为NNN 的字符(1 至3 个数位)
  \\		反斜杠
  \a		终端鸣响
  \b		退格
  \f		换页
  \n		换行
  \r		回车
  \t		水平制表符
  \v		垂直制表符
  字符1-字符2	从字符1 到字符2 的升序递增过程中经历的所有字符
  [字符*]	在SET2 中适用，指定字符会被连续复制直到吻合设置1 的长度
  [字符*次数]	对字符执行指定次数的复制，若次数以 0 开头则被视为八进制数
  [:alnum:]	所有的字母和数字
  [:alpha:]	所有的字母
  [:blank:]	所有呈水平排列的空白字符
  [:cntrl:]	所有的控制字符
  [:digit:]	所有的数字
  [:graph:]	所有的可打印字符，不包括空格
  [:lower:]	所有的小写字母
  [:print:]	所有的可打印字符，包括空格
  [:punct:]	所有的标点字符
  [:space:]	所有呈水平或垂直排列的空白字符
  [:upper:]	所有的大写字母
  [:xdigit:]	所有的十六进制数
  [=字符=]	所有和指定字符相等的字符
```

| 选项                 | 说明                             |
| -------------------- | -------------------------------- |
| -d, --delete         | 删除所有第一字符集的所有字符     |
| -c, -C, --complement | 以set2替换不属于第一字符集的字符 |
|                      |                                  |

### 示例

~~~shell
# 删除所有字母，有多种写法
tr -d [A-z]
tr -d 'A-z'
tr -d [:alpha:]

# 删除除字母和数字之外的所有字符，可以理解为这里的-c对-d起到了一个取反的作用。
echo 'AbcdE123456@#' | tr -dc [A-z,0-9]

# 删除'123'
echo 'a1b2d3' | tr -d 123

# 把@、%、#替换为空格
echo '!@#$%^&*()_/' | tr @%# ' '
~~~
