## docker build命令

构建镜像

### 用法
```
docker build [OPTIONS] PATH | URL | -
```
| 选项 | 说明 |
| --- | --- |
| -t          | 指定镜像名，格式为name:tag，tag缺省为latest                  |
| --build-arg | 设置构建时的变量。--build-arg https_proxy=http://XXX:port，多个变量写多个--build-arg |
| --add-host  | 添加一个自定义主机到ip的映射(host:ip)                        |
| -q          | 安静模式，关闭构建输出，仅在成功后打印镜像ID                 |
| -c          | cpu权重                                                      |
| -m          | 限制内存                                                     |

### 示例
```sh
# 通过当时目录下名为 dockerfile 的文件构建一个镜像，名为nginx
# .表示在当前目录下搜索dockerfile文件。
docker build -t nginx .
```