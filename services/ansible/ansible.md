## ansible命令
针对一组主机定义并运行单个任务“剧本”
### 用法
```shell
ansible [-h]
        [--version]
        [-v]
        [-b]
        [--become-method BECOME_METHOD]
        [--become-user BECOME_USER]
        [-K | --become-password-file BECOME_PASSWORD_FILE]
        [-i INVENTORY]
        [--list-hosts]
        [-l SUBSET]
        [-P POLL_INTERVAL]
        [-B SECONDS]
        [-o]
        [-t TREE]
        [--private-key PRIVATE_KEY_FILE]
        [-u REMOTE_USER]
        [-c CONNECTION]
        [-T TIMEOUT]
        [--ssh-common-args SSH_COMMON_ARGS]
        [--sftp-extra-args SFTP_EXTRA_ARGS]
        [--scp-extra-args SCP_EXTRA_ARGS]
        [--ssh-extra-args SSH_EXTRA_ARGS]
        [-k | --connection-password-file CONNECTION_PASSWORD_FILE]
        [-C]
        [--syntax-check]
        [-D]
        [-e EXTRA_VARS]
        [--vault-id VAULT_IDS]
        [--ask-vault-password | --vault-password-file VAULT_PASSWORD_FILES]
        [-f FORKS]
        [-M MODULE_PATH]
        [--playbook-dir BASEDIR]
        [--task-timeout TASK_TIMEOUT]
        [-a MODULE_ARGS]
        [-m MODULE_NAME]
        pattern
```

| 选项 | 说明 |
| ---                                                                   | --- |
| -i INVENTORY, --inventory INVENTORY, --inventory-file INVENTORY       | 指定主机清单文件，或者以逗号隔开的主机列表
| -m MODULE_NAME, --module-name MODULE_NAME                             | 指定模块
| -u \<REMOTE_USER\>                                                    | 以该用户身份连接
| --become-user BECOME_USER                                             | 指定become user
| -b, --become                                                          | 使用become
| -K, --ask-become-pass                                                 | 指定密码
| -m \<MODULE_NAME\>                                                    | 要执行的模块，默认是command
| -a MODULE_ARGS, --args MODULE_ARGS                                    | 模块参数
| -e EXTRA_VARS, --extra-vars EXTRA_VARS                                | 设置变量，格式为key=value
| -C, --check                                                           | 不做任何更改，只预测会发生哪些变化
| --syntax-check                                                        | 对剧本进行语法检查，但不执行它
| --list-hosts                                                          | 仅输出所匹配主机的列表
| -l SUBSET, --limit SUBSET                                             | 进一步限制主机
| -v                                                                    | 详细模式，-vvvv用于启用连接调试
| -T TIMEOUT, --timeout TIMEOUT                                         | 以秒为单位覆盖连接超时时间（默认值=10）
| -f FORKS, --forks FORKS                                               | 指定要使用的并行进程数（默认值为5）

### 示例
```sh
# 在远程主机上执行命令，默认使用cmd模块
ansible -i hosts -a 'ls /root'

```
