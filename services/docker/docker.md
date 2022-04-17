## docker search&

在docker hub中搜索镜像

### 用法

Usage:	docker search [Options] TERM

| 选项 | 说明 |
| --- | --- |
| --limit int | 限制搜索结果数量 |
| --no-trunc | 不截断输出 |

### 示例
```shell
# 搜索nginx镜像
docker search nginx
```

## 推送镜像docker push&

推送镜像。将镜像推到注册表（docker hub或者私有registry）。

### 用法

docker push [Options] NAME[:TAG]

| 选项 | 说明 |
| --- | --- |
| --disable-content-trust | 跳过镜像签名（默认为真），用不到 |

### 示例
```shell
# 推送指定镜像
docker push yudeyu/nginx:1.17.10
```

## 镜像拉取docker pull&

从注册表中提取镜像或存储库拉取镜像

### 用法

docker pull [Options] NAME[:TAG|@DIGEST]

| 选项 | 说明 |
| --- | --- |
| -q | 不详细输出拉取过程 |
| -a | 下载存储库中所有镜像 |

### 示例
```shell
# 从默认仓库拉取mysql的最新镜像
docker pull mysql

# 拉取指定版本的nginx镜像，并且不详细输出拉取过程
docker pull –q nginx:1.17.10
```
 
## docker load&

从tar存档或STDIN加载镜像。

注：通过export导出的镜像，不可以使用load加载，应该用import导入。

### 用法

docker load [Options]

| 选项 | 说明 |
| --- | --- |
| -i | 指定从tar存档文件(而不是STDIN)读取 |
| -q | 不输出导入过程 |

### 示例
```shell
# 从/root/test.tar导入镜像，不显示导入过程。
docker load –qi /root/test.tar
```

## docker import

## docker export&

将容器的文件系统导出为tar归档文件。

该方式保存的是容器，所以对容器相应的修改也会保存下来。

注：此方式导出的镜像归档文件，需用docker import导入，不能用docker load。

### 用法

docker export [Options] CONTAINER

| 选项 | 说明 |
| --- | --- |
| -o | 指定镜像导出的位置 |

### 示例
```shell
# 将名为nginx容器导出，保存到当前目录下为nginx.tar
docker export nginx -o nginx.tar
```

## docker images&

列出镜像

### 用法

docker images [Options] [REPOSITORY[:TAG]]

| 选项 | 说明 |
| --- | --- |
| -a | 显示所有镜像(默认隐藏中间镜像) |
| -q | 只显示镜像的ID。 |
| --no-trunc | 不截断输出。可以显示镜像完整ID。 |

### 示例
```shell
# 查看本地镜像
docker images

# 查看镜像，只显示镜像ID
docker images –q
```

## docker rmi&

移除一个或多个镜像

### 用法

docker rmi [Options] IMAGE [IMAGE...]

| 选项 | 说明 |
| --- | --- |
| -f | 强制移除镜像。镜像被某个窗口使用时需要加该选项。 |

### 示例
```shell
# 删除nginx和mysql镜像
docker rmi nginx mysql

# 强制删除一个镜像
docker rmi –f nginx:1.17.10

# 命令嵌套。删除所有未被使用的镜像
docker rmi `docker images -q`  
```
## docker build

### 用法

docker build [OPTIONS] PATH | URL | -

| 选项 | 说明 |
| --- | --- |
| -t          | 指定镜像名，格式为name:tag，tag缺省为latest                  |
| --build-arg | 设置构建时的变量。--build-arg https_proxy=http://XXX:port，多个变量写多个--build-arg |
| --add-host  | 添加一个自定义主机到ip的映射(host:ip)                        |
| -q          | 安静模式，关闭构建输出，仅在成功后打印镜像ID                 |
| -c          | cpu权重                                                      |
| -m          | 限制内存                                                     |

### 示例
```shell
docker build -t nginx .
```
.表示在当前目录下搜索dockerfile文件。

## docker commit

## docker tag&

参照一个源镜像来创建一个新的镜像

用来修改镜像的名字或者标签，改完后把源镜像删除即可。

### 用法

docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

### 示例
```shell
# 修改tag
docker tag nginx yudeyu/nginx:1.17.10
```
## docker cp&

在容器和本地文件系统之间复制文件

### 用法
```
# 从容器往本地复制
docker cp [Options] CONTAINER:SRC_PATH DEST_PATH|-

# 从本地往容器复制
docker cp [Options] SRC_PATH|- CONTAINER:DEST_PATH
```

| 选项 | 说明 |
| --- | --- |
| -a | 存档模式（复制所有uid / gid信息） |
| -L | 始终遵循SRC_PATH中的符号链接|

### 示例
```shell
# 将容器nginx中的/etc/hosts文件复制到当前目录
docker cp nginx:/etc/hosts ./
```
## docker ps&

列出容器

### 用法

docker ps [Options]

| 选项 | 说明 |
| --- | --- |
| -a | 显示所有状态的容器（默认仅显示状态为running的） |
| -n | 显示最后创建的N个容器（包括所有状态） |
| -l | 显示最新创建的1容器（包括所有状态） |
| --no-trunc | 不截断容器ID  |
| -q | 只显示容器ID |
| -s | Display total file sizes |

### 示例
```shell
# 显示状态为running的容器
docker ps

# 显示最后创建的10个容器，包括所有状态的
docker ps -n10

# 显示所有状态的容器的ID
docker ps -aq
```
## docker rm&

移除一个或多个容器

### 用法

docker rm [Options] CONTAINER [CONTAINER...]

| 选项 | 说明 |
| --- | --- |
| -f | 强制移除容器 |
| -v | 删除与容器关联的匿名卷 |

### 示例
```shell
# 强制移除名为nginx的容器
docker rm –f nginx
```
## docker create

创建一个新容器

### 用法

docker create [Options] IMAGE [COMMAND] [ARG...]

| 选项 | 说明 |
| --- | --- |
| -a |  |
| -c |  |
| -e | 设置变量 |
| --env-file | 从文件读取变量 |
| -h | 设置容器主机名 |
| -v | 绑定挂载卷 |
| -p | 将容器的端口发布到主机，-p 本地端口:容器端口 |
| -w | 设置容器内的工作目录 |
| -u | 设置用户 |
| --name | 设置容器名 |
| --rm | 当容器退出时自动删除它 |
| --read-only | 将容器的根文件系统设置为只读 |
| --restart | 设置容器退出时的重启策略（默认为no），策略有以下五种 |

| 策略 | 说明 |
| --- | --- |
| no             | 默认策略，在容器退出时不重启容器                             |
| always         | 在容器退出时总是重启容器                                     |
| on-failure     | 在容器非正常退出时（退出状态非0），才会重启容器              |
| on-failure:N   | 在容器非正常退出时重启容器，最多重启N次                      |
| unless-stopped | 在容器退出时总是重启容器，但是不考虑在Docker守护进程启动时就已经停止了的容器 |


### 示例

## docker start&

启动一个或多个容器

### 用法

docker start [Options] CONTAINER [CONTAINER...]

| 选项 | 说明 |
| --- | --- |
| -a | 绑定容器的输出 |
| -i | 绑定标准输入 |

### 示例
```shell
# 启动nginx mysql容器
docker start nginx mysql
```
## 运行容器docker run

run是create和start的组合

### 用法

docker run [Options] IMAGE [COMMAND] [ARG...]

选项几乎和create一样，只是多了下面几个选项。

| 选项 | 说明 |
| --- | --- |
| -d | 后台启动容器，并返回容器ID。 |

## 更新容器配置docker update

更新一个或多个容器的配置

### 用法

docker update [Options] CONTAINER [CONTAINER...]

| 选项 | 说明 |
| --- | --- |
| -c | |
| -m | 内存限制 | 
| --restart | 重启策略 |

### 示例

## 停止容器docker stop&

停止运行一个或多个容器

### 用法

docker stop [Options] CONTAINER [CONTAINER...]

| 选项 | 说明 |
| --- | --- |
| -t | 在杀死容器之前等待的秒数（默认为10）。指容器不能正常停止，需要强制杀死所等待的时间。 |

### 示例
```shell
# 将名为nginx的容器停止
docker stop nginx
```
## docker restart&

重启一个或多个容器。实际就是先执行stop再执行start。

### 用法

docker restart [Options] CONTAINER [CONTAINER...]

| 选项 | 说明 |
| --- | --- |
| -t | 在杀死容器之前等待的秒数（默认为10）。指容器不能正常停止，需要强制杀死所等待的时间。 |

### 示例
```shell
# 重启容器
docker restart mysql
```
## docker exec&

在运行的容器中运行命令。

### 用法

docker exec [Options] CONTAINER COMMAND [ARG...]

| 选项 | 说明 |
| --- | --- |
| -i | 让容器的标准输入保持打开(即交互式)。 |
| -t | 让 Docker分配一个伪终端（pseudo-tty）并绑定到容器的标准输入上 |
| -e | 设置环境变量。例如：-e E1=1 |
| -w | 设置容器的工作目录。例如：-w /etc |
| -u | 指定用户，可以写用户名或UID |

### 示例
```shell
# 打印nginx这个容器的PATH变量
docker exec nginx echo $PATH

# 进入到centos这个容器当中
docker exec -it centos bash
```

## 进入容器docker attach

attach和exec功能类似，不同的是attach 直接进入容器启动命令的终端，不会启动新的进程，exec 则是在容器中打开新的终端，并且可以启动新的进程。

## docker pause&

暂停一个或多个容器中的所有进程

### 用法

docker pause CONTAINER [CONTAINER...]

## docker unpause&

恢复一个或多个容器中的所有进程

### 用法

docker unpause CONTAINER [CONTAINER...]

## docker logs&

获取容器日志

### 用法

docker logs [Options] CONTAINER

| 选项 | 说明 |
| --- | --- |
| -f | 跟踪日志输出 |
| -t | 显示时间戳 |

### 示例

docker logs -f mysql  # 查看mysql的日志，并且跟踪后续输出内容。

## docker inspect&

返回docker对象的详细信息

docker对象包括`containers`,`images`,`volume`,`network`等信息
### 用法

docker inspect [Options] NAME|ID [NAME|ID...]

### 示例
```shell
# 查看容器信息
docker inspect CONTAINERS

# 查看镜像的信息
docker inspect IMAGES  
```
