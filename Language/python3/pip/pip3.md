## pip3命令

```sh
# 使用指定的源
# 清华大学源
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ some-package
# 阿里云源
pip3 install -i https://mirrors.aliyun.com/pypi/simple/ some-package

# 永久修改源
pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/


# 安装指定版本的包
pip3 install package_name==version

# 通过本地归档文件安装一个包和它的依赖
pip3 install ./downloads/packge-1.0.1.tar.gz ./downloads/depend.tar.gz



# 使用whl文件安装
pip3 install openpyxl-3.1.5-py2.py3-none-any.whl et_xmlfile-1.1.0-py3-none-any.whl
```


```py
# 查看支持安装什么平台的包
import pip
import pip3
print(pip.pep425tags.get_supported())
```