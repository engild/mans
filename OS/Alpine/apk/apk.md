## apk命令


### 仓库配置路径
/etc/apk/repositories


### apk加速
```sh
# 修改为使用阿里云镜像源
sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
```
