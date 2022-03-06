# groupmod命令&

用于修改组

## 用法

groupmod [选项] 组名

| 选项                       | 说明                |
| -------------------------- | ------------------- |
| -g, --gid <GID>            | 修改组ID为GID       |
| -n, --new-name <NEW_GROUP> | 修改组名为NEW_GROUP |
| -o, --non-unique           | 允许使用重复的 GID  |

## 示例

~~~shell
# 将组ID为500的修改成组ID为1500
groupmod -g 1500 500

# 将组名test1_group修为为test2_group
groupmod -n test2_group test1_group
~~~
