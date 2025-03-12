## cat命令

连接文件并在标准输出上打印，或者将标准输入连接到标准输出。

### 用法
```
cat [OPTION]... [FILE]...
```


-n  # 输出时显示行号。


```sh
# 直接将文本追加到文件中。如果是覆盖，cat后面写一个>
cat >> /tmp/yourfile << EOF
Your content
EOF

# 直接将文本写到文件中无权限时：
sudo bash -c "cat > /etc/hosts" << EOF
Your content
EOF

#

```