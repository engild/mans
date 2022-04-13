# usermod&

修改用户账户

## 用法

usermod [选项] 用户名

| 选项 | 说明                                                         |
| ---- | ------------------------------------------------------------ |
| -d   | 修改用户的宿主目录，-d  /home/user1                          |
| -m   | 将用户主目录的内容移动到新位置。如果当前主目录不存在，则不会创建新的主目录。此选项仅在与-d选项组合时有效。 |
| -l   | 修改用户名，-l  新用户名                                     |
| -u   | 修改用户ID，-u  新ID                                         |
| -s   | 修改用户登录shell，-s  登录shell                             |
| -e   | 修改用户到期时间                                             |
| -g   | 修改用户所属的组，-g  新组                                   |
| -G   | 将用户添加到-G指定的多个组当中，以逗号隔开，-G root,wheel,test |
| -a   | 将用户附加到-G指定的组当中，而不会将其从其他组中移除。       |
| -L   | 锁定用户                                                     |
| -U   | 解锁                                                         |

## 示例

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
