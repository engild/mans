## host命令

## Usage
```
host [-aCdilrTvVw] [-c class] [-N ndots] [-t type] [-W time]
            [-R number] [-m flag] hostname [server]
```



```sh
# 使用grep命令仅过滤出来IP
host -W 3 hostname | grep -oP 'has address \K\S+'
```
