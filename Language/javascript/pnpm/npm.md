npm命令

```sh
# 获取配置
npm config get registry

# 设置为官方源
npm config set registry https://registry.npmjs.org

# 设置为华为源
npm config set registry https://mirrors.huaweicloud.com/repository/npm/

# 清缓存
npm cache clean --force
```


## 报错
WARN  GET https://registry.npm.taobao.org/jsdom error (CERT_HAS_EXPIRED)

换成华为源