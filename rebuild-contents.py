#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import re

# init
server = "https://github.com"
author = "engild"
repo = "mans"
repo_url = f"{server}/{author}/{repo}/"
ignore_files = ["branch", "README.md", "translate.json", "command-example.md", os.path.basename(__file__)]

script_directory = os.path.dirname(os.path.abspath(__file__))
with open(script_directory + '/branch', 'r') as file:
    branch = file.read()

def is_done_command(file):   # done
    # 判断命令是否已整理完成
    command_name, description = False, False
    title_re = "^## (.*)命令&$"
    describe_re = "^说明[:：] ?(.*)"
    
    with open(file, "r") as f:
        content = f.readlines()
    
    if len(content) >= 2:
        title = content[0]
        describe = content[1]
    else:
        return False

    # 如果命令已整理完成，提取命令
    title_match = re.search(title_re, title)
    if title_match:
        command_name = title_match.group(1)
        
    # 如果已写说明，提取说明
    description_match = re.search(describe_re, describe)
    if description_match:
        description = description_match.group(1)
    
    # 如果命令已整理完成，返回命令和说明
    if command_name and description:
        return command_name, description
    else:
        return False

def gen_link(file):   # done
    # 生成链接
    new_path = file.replace(script_directory, "")
    if os.path.isfile(file):
        t = "blob/"
    elif os.path.isdir(file):
        t = "tree/"
    else:
        print("This is neither a file nor a directory.")
        return None
    
    link = repo_url + t + branch + new_path
    
    return link

def get_translate(translate_file):   # done
    try:
        with open(translate_file, "r", encoding="utf-8") as file:
            data = json.load(file)
    except:
        return {}
    
    return data

def get_all(path):   # done
    # 获取路径下所有文件和目录
    all_items = os.listdir(path)
    
    # 获取路径下所有非隐藏的目录
    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item)) and not item.startswith('.')]
    
    # 获取路径下所有非隐藏的文件
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item)) and not item.startswith('.')]
    files = [i for i in files if i not in ignore_files]

    return path, sorted(directories), files

def write_readme(content, file):   # done
    if content:
        with open(file, "w") as f:
            for item in content:
                f.write(f"{item}\n")

def process_c(root, dir):   # done
    readme_file = root + "/" + dir + "/README.md"
    readme_content = []
    
    # 获取目录下的目录和文件
    nroot, dirs, files = get_all(root + "/" + dir)
    
    # 如果路径下有目录，获取说明
    if dirs:
        translate_file = nroot + "/translate.json"
        explains = get_translate(translate_file)

        
        # 遍历目录，生成目录的链接（1级）
        for d in dirs:
            link = gen_link(nroot + "/" + d)
            explain = explains.get(d, "")
            if explain:
                content = f"### [{d} —— {explain}]({link})"
            else:
                content = f"### [{d}]({link})"
            readme_content.append(content)
            process_c(nroot, d)
            
            # 添加二级链接
            next_root2, dirs2, files2 = get_all(nroot + "/" + d)
            # 添加目录
            if dirs2:
                translate_file2 = next_root2 + "/translate.json"
                explains2 = get_translate(translate_file2)
                for d2 in dirs2:
                    link2 = gen_link(next_root2 + "/" + d2)
                    explain2 = explains.get(d2, "")
                    if explains2:
                        content2 = f"- [{d2} —— {explain2}]({link2})"
                    else:
                        content2 = f"- [{d2}]({link2})"
                    readme_content.append(content2)
            # 添加文件
            if files2:
                for f2 in files2:
                    file2 = next_root2 + "/" + f2
                    ret2 = is_done_command(file2)
                    if ret2:
                        title2 = ret2[0]
                        explain2 = ret2[1]
                        link2 = gen_link(file2)
                        content2 = f"- [{title2} —— {explain2}]({link2})"
                        readme_content.append(content2)
    
    # 遍历文件，生成文件的链接（1级）
    if files:
        for f in files:
            file = nroot + "/" + f
            ret = is_done_command(file)
            if ret:
                title = ret[0]
                explain = ret[1]
                link = gen_link(file)
                content = f"- [{title} —— {explain}]({link})"
                readme_content.append(content)
            
    # 最终内容写入readme文件
    if readme_content:
        write_readme(readme_content, readme_file)
 

def main():
    script_root, script_dir, script_file = get_all(script_directory)
    for dir in script_dir:
        process_c(script_root, dir)

if __name__ == '__main__':
    main()
