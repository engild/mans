import os

# 获取当前脚本的绝对路径
current_script_path = os.path.abspath(__file__)
print("当前脚本的绝对路径:", current_script_path)

# 获取当前脚本的目录路径
current_script_dir = os.path.dirname(os.path.abspath(__file__))
print("当前脚本的目录路径:", current_script_dir)
