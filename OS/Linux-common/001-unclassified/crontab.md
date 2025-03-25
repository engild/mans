## crontab命令
-u USER   # 指定用户，缺省为当前用户。
-l   # 显示当前计划任务。
-e   # 编辑计划任务。
-r   # 移除计划任务，慎用。
-i   # 使用-r选项时，会向用户确认是否移除。

### 示例
```sh
# 编辑test用户的定时任务
crontab -eu test

# 删除包含delete_cron的任务
crontab -l | grep -v delete_cron | crontab
```

### 定时任务示例
```

```
