## usermod命令&
说明: 修改用户账户

### 用法
```shell
usermod [options] LOGIN

# LOGIN表示用户名
```

| 选项 | 说明 |
| ---- | --- |
| -d, --home HOME_DIR           | 修改用户的宿主目录
| -m, --move-home               | 将用户主目录的内容移动到新位置。如果当前主目录不存在，则不会创建新的主目录。此选项仅在与-d选项组合时有效。
| -l, --login NEW_LOGIN         | 修改用户名
| -u, --uid UID                 | 修改用户ID
| -s, --shell SHELL             | 修改用户登录shell
| -e, --expiredate EXPIRE_DATE  | 修改用户到期时间为EXPIRE_DATE
| -g, --gid GROUP               | 修改用户所属的组
| -G, --groups GROUPS           | 将用户添加到-G指定的多个组当中，以逗号隔开
| -a, --append GROUP            | 将用户附加到-G指定的组当中，而不会将其从其他组中移除。
| -L, --lock                    | 锁定用户
| -U, --unlock                  | 解锁用户

### 示例

```shell
# 锁定test用户
usermod -L test

# 为test用户解锁
usermod -U test

# 将test用户名改为test1
usermod -l test1 test

# 将test用户的ID改为1010
usermod -u 1010 test

# 将test用户的登录shell设置为/bin/false，意为不可登录。
usermod -s /bin/false test

# 将test用户的宿主目录修改为new_home,同时会将原宿主目录名修改为new_home。
usermod -md new_home test
```
