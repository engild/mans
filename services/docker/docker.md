# docker命令

# 通过overlay目录查所属容器
docker ps -q | xargs docker inspect --format '{{.State.Pid}}, {{.Id}}, {{.Name}}, {{.GraphDriver.Data.WorkDir}}' | grep

## docker attach命令

attach和exec功能类似，不同的是attach 直接进入容器启动命令的终端，不会启动新的进程，exec 则是在容器中打开新的终端，并且可以启动新的进程。
---

## docker commit命令
---

## docker create命令

创建一个新容器

### 用法
```
docker create [Options] IMAGE [COMMAND] [ARG...]
```
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
---
## docker exec命令&

在运行的容器中运行命令。

### 用法
```
docker exec [Options] CONTAINER COMMAND [ARG...]

CONTAINER可以是容器的名字，也可以是容器的ID
```

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
---

## docker import命令

## docker load命令&

从`tar`存档或`STDIN`加载镜像。

注：通过export导出的镜像，不可以使用load加载，应该用import导入。

### 用法
```
docker load [Options]
```

| 选项 | 说明 |
| --- | --- |
| -i | 指定从tar存档文件(而不是STDIN)读取 |
| -q | 不输出导入过程 |

### 示例
```shell
# 从/root/test.tar导入镜像，不显示导入过程。
docker load -qi /root/test.tar
```
---
## docker pause命令&

暂停一个或多个容器中的所有进程

### 用法
```
docker pause CONTAINER [CONTAINER...]
```
---

---
## docker pull命令&

从注册表中提取镜像或存储库拉取镜像

### 用法
```
docker pull [Options] NAME[:TAG|@DIGEST]
```

| 选项 | 说明 |
| --- | --- |
| -q | 不详细输出拉取过程 |
| -a | 下载存储库中所有镜像 |

### 示例
```shell
# 从默认仓库拉取mysql的最新镜像
docker pull mysql

# 拉取指定版本的nginx镜像，并且不详细输出拉取过程
docker pull -q nginx:1.17.10
```
---
## docker push命令&

推送镜像。将镜像推到注册表（`docker hub`或者私有`registry`）。

### 用法
```
docker push [Options] NAME[:TAG]
```

| 选项 | 说明 |
| --- | --- |
| --disable-content-trust | 跳过镜像签名（默认为真），用不到 |

### 示例
```shell
# 推送指定镜像
docker push yudeyu/nginx:1.17.10
```
---
## docker restart命令&

重启一个或多个容器。实际就是先执行`stop`再执行`start`。

### 用法
```
docker restart [Options] CONTAINER [CONTAINER...]
```

| 选项 | 说明 |
| --- | --- |
| -t | 在杀死容器之前等待的秒数（默认为10）。指容器不能正常停止，需要强制杀死所等待的时间。 |

### 示例
```shell
# 重启容器
docker restart mysql
```
---
## docker rmi命令&

移除一个或多个镜像

### 用法
```
docker rmi [Options] IMAGE [IMAGE...]
```

| 选项 | 说明 |
| --- | --- |
| -f | 强制移除镜像。镜像被某个窗口使用时需要加该选项。 |

### 示例
```shell
# 删除nginx和mysql镜像
docker rmi nginx mysql

# 强制删除一个镜像
docker rmi -f nginx:1.17.10

# 命令嵌套。删除所有未被使用的镜像
docker rmi `docker images -q`
```
---
## docker rm命令&

移除一个或多个容器

### 用法
```
docker rm [Options] CONTAINER [CONTAINER...]
```
| 选项 | 说明 |
| --- | --- |
| -f | 强制移除容器 |
| -v | 删除与容器关联的匿名卷 |

### 示例
```shell
# 强制移除名为nginx的容器
docker rm -f nginx
```
---
## 运行容器docker run

`docker run`是`docker create`和`docker start`的组合
### 用法
```
docker run [Options] IMAGE [COMMAND] [ARG...]

选项几乎和docker create一样，只是多了下面几个选项。
```

| 选项 | 说明 |
| --- | --- |
| -d | 后台启动容器，并返回容器ID。 |
---
## docker search命令&

在`docker hub`中搜索镜像

### 用法
```
Usage:	docker search [Options] TERM
```

| 选项 | 说明 |
| --- | --- |
| --limit int | 限制搜索结果数量 |
| --no-trunc | 不截断输出 |

### 示例
```shell
# 搜索nginx镜像
docker search nginx
```
---
## docker start命令&

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
---
## docker stop命令&

停止运行一个或多个容器

### 用法
```
docker stop [Options] CONTAINER [CONTAINER...]
```

| 选项 | 说明 |
| --- | --- |
| -t | 在杀死容器之前等待的秒数（默认为10）。指容器不能正常停止，需要强制杀死所等待的时间。 |

### 示例
```shell
# 将名为nginx的容器停止
docker stop nginx
```
---
## docker tag命令&

参照一个源镜像来创建一个新的镜像

用来修改镜像的名字或者标签，改完后把源镜像删除即可。

### 用法
```
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
```

### 示例
```shell
# 修改tag
docker tag nginx yudeyu/nginx:1.17.10
```
---
## docker unpause命令&

恢复一个或多个容器中的所有进程

### 用法
```
docker unpause CONTAINER [CONTAINER...]
```
---
## docker update命令

更新一个或多个容器的配置

### 用法
```
docker update [Options] CONTAINER [CONTAINER...]
```
| 选项 | 说明 |
| --- | --- |
| -c | |
| -m | 内存限制 |
| --restart | 重启策略 |

### 示例

