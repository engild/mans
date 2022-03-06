from importlib.resources import contents
from logging import exception
import os

server = "https://github.com"
author = "engild"
repo = "mans"
repo_url = "%s/%s/%s" %(server, author, repo)
branch_name = open('branch-name', 'r').read()


def get_subdir(path):   
    contents_file = open(path + '/README.md', 'w', encoding='utf-8')
    info = os.walk(path)
    translate_file = open(path + '/translate', 'r').read()
    translate = eval(translate_file)
    for current_dir, subdir, file_list in info:
        if current_dir == path:
            continue
        
        link_name = current_dir[current_dir.find('/') + 1:]
        dir_link = "### [%s](%s/tree/%s/%s)\n" %(translate.get(link_name, link_name), repo_url, branch_name, current_dir)
        contents_file.write(dir_link)

        for f in file_list:
            link = "- [%s] (%s/blob/%s/%s/%s)\n" %(f[:f.rfind('.')], repo_url, branch_name, current_dir, f)
            contents_file.write(link)

    contents_file.close()


dirs = [
    'Debian-family-system-commands', 
    'Linux-system-common-commands', 
    'Redhat-family-system-commands',
    ]

for i in dirs:
    get_subdir(i)


# <!--
# https://github.com/engild/mans/tree/master/Linux-system-common-commands
# -->





    
