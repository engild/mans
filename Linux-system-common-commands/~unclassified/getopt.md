## xxx命令
这里写命令的简单说明

### 用法
```
xxx [选项]
```

| 选项 | 说明 |
| --- | --- |
| -a, --alternative | 允许长选项以单个“-”开头。 |
| -o, --options shortopts |  |
| -l, --longoptions longopts |  |

### 示例
```sh
# 短格式无参数选项
args=`getopt adp $*`
while :; do
    case "$1" in
    -d)
        echo option $1 is seted
        shift
        ;;
    -a)
        echo option $1 is seted
        shift
        ;;
    -p)
        echo option $1 is seted
        shift
        ;;
    --)
        shift; break
        ;;
    esac
done

# 调用
./script_name -a -p
./script_name -adp
------------------------------------------------------------------------------

# 短格式带参数选项
args=`getopt q:w: $*`
while :; do
    case "$1" in
    -q)
        echo key $1 value $2
        shift; shift
        ;;
    -w)
        echo key $1 value $2
        shift; shift
        ;;
    --)
        shift; break
        ;;
    esac
done

# 调用
./script_name -q value1 -w value2

```
