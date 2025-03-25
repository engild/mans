## ansible-playbook命令
运行ansible剧本的工具

### 用法
```shell
ansible-playbook [-h]
                 [--version]
                 [-v]
                 [--private-key PRIVATE_KEY_FILE]
                 [-u REMOTE_USER]
                 [-c CONNECTION]
                 [-T TIMEOUT]
                 [--ssh-common-args SSH_COMMON_ARGS]
                 [--sftp-extra-args SFTP_EXTRA_ARGS]
                 [--scp-extra-args SCP_EXTRA_ARGS]
                 [--ssh-extra-args SSH_EXTRA_ARGS]
                 [-k | --connection-password-file CONNECTION_PASSWORD_FILE]
                 [--force-handlers]
                 [--flush-cache]
                 [-b]
                 [--become-method BECOME_METHOD]
                 [--become-user BECOME_USER]
                 [-K | --become-password-file BECOME_PASSWORD_FILE]
                 [-t TAGS]
                 [--skip-tags SKIP_TAGS]
                 [-C]
                 [--syntax-check]
                 [-D]
                 [-i INVENTORY]
                 [--list-hosts]
                 [-l SUBSET]
                 [-e EXTRA_VARS]
                 [--vault-id VAULT_IDS]
                 [--ask-vault-password | --vault-password-file VAULT_PASSWORD_FILES]
                 [-f FORKS]
                 [-M MODULE_PATH]
                 [--list-tasks]
                 [--list-tags]
                 [--step]
                 [--start-at-task START_AT_TASK]
                 playbook [playbook ...]
```

| 选项 | 说明 |
| -------------- | ------------ |
| -i                          | 指定清单主机路径或逗号分隔的主机列表                         |
| --syntax-check              | 仅做语法检测                                                 |
| -u \<REMOTE_USER>            | 以该用户身份连接                                             |
| --become-user \<BECOME_USER> | 以该用户身份运行操作，默认为root                             |
| --step                      | 步进模式，一步一步执行：在每个任务运行之前都会确认，(y/n/c)回答“ y”以执行任务，回答“ n”以跳过任务，回答“ c”以退出步进模式，无需询问即可执行所有其余任务。 |
| -C                          | 不要做任何改变；相反，尝试预测可能发生的某些变化             |
| --verbose                   | 详细输出                                                     |
| --list-host                 | 仅输出所匹配主机列表                                         |
| -l SUBSET, --limit SUBSET   | 进一步限制哪些主机可以执行任务                               |
| --list-tags                 | 列出所有可用标签                                             |
| --list-tasks                | 列出将要执行的所有任务                                       |
| -v                          | 详细模式（-vvv用于更多，-vvvv用于启用连接调试）              |
| -f FORKS                    | 指定并行进程数，默认为5                                      |
| --start-at-task=            | 指定从哪个任务开始，通常是上次运行失败的任务                 |

### 示例

运行一个剧本，并设置并行进程为10

```shell
ansible-playbook playbook.yml -f 10
```
