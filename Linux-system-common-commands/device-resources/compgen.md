## compgen命令

### 用法
```
compgen [-abcdefgjksuv] [-o option]  [-A action] [-G globpat] [-W wordlist]  [-F function] [-C command] [-X filterpat] [-P prefix] [-S suffix] [word]
```

| 选项 | 说明                             |
| ---- | -------------------------------- |
| -a   | 显示系统中所有的别名             |
| -b   | 显示系统内建命令                 |
| -c   | 显示系统中所有的命令（有重复的） |
| -g   | 显示系统中所有的组名             |
| -u   | 显示系统中所有的用户名           |
| -v   | 显示系统中所有变量名             |

### 示例
~~~shell
# 显示所有用户
compgen -u

# 显示所有组
compgen -g
~~~
