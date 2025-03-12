# shell语法


## case
```sh
case VAR in
    mode1)
        commands
    ;;

    mode2)
        commands
    ;;

    *)
        commands
esac
```

## if判断

```sh
# 文件存在返回True
if [ -f ${FILE} ]; then
    echo ${FILE} exist
fi

# 大于返回True
if [ 1 -gt 0 ]; then
    echo ok
fi
# 大于 -gt (greater than)
# 小于 -lt (less than)
# 大于或等于 -ge (greater than or equal)
# 小于或等于 -le (less than or equal)
# 不等于 -ne （not equal）
# 等于 -eq （equal）





```

