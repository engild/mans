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
| -------------- | ------------------------------------------ |
| -i                 | 指定主机清单文件，或者以逗号隔开的主机列表 |
| -u \<REMOTE_USER\> | 以该用户身份连接                           |
| -k                 | 指定密码                                   |
| -m \<MODULE_NAME\> | 要执行的模块，默认是command                |
| -a                 | 模块参数                                   |
| -C                 | 不做任何更改，只预测会发生哪些变化         |
| --syntax-check     | 对剧本进行语法检查，但不执行它             |
| --list-hosts       | 仅输出所匹配主机的列表                     |
| -v                 | 详细模式，-vvvv用于启用连接调试            |
|                    |                                            |

### 示例
```shell
```
