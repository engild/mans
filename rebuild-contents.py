#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json

server = "https://github.com"
author = "engild"
repo = "mans"
repo_url = "%s/%s/%s/" %(server, author, repo)
ignore_files = ['branch', 'README.md', 'translate', os.path.basename(__file__)]
print(ignore_files)
# print(os.path.basename(__file__))
c_dir = os.path.dirname(os.path.abspath(__file__)) + '/'

with open(c_dir + 'branch', 'r') as file:
    branch = file.read()

def read_json(path):
    try:
        with open(path, 'r') as file:
            result = json.load(file)
    except Exception as e:  
        result = False
    return result
    
def pad_str(*args, length=40, char='-'):
    for i in args:
        # length = length - len(i.encode('utf-8'))
        length = length - len(i.encode('GBK'))
    if length > 0:
        try:
            result = args[0] + (char * length) + args[1]
        except IndexError:
            result = args[0] + (char * length)
    return result
    
def gen_link(path):
    if os.path.isfile(c_dir + path):
        t = 'blob/'
    elif os.path.isdir(c_dir + path):
        t = 'tree/'
    else:
        print("This is neither a file nor a directory.")
    result = repo_url + t + branch + '/' + path
    return result

def hh():
    translate = read_json(c_dir + 'translate')
    for k, v in translate.items():
        link = gen_link(k)
        name = pad_str(k, v, length=25)
        s1 = "### [%s](%s)" %(name, link)
        print(s1)
        sub_translate_path = os.path.join(c_dir + k, 'translate')
        sub_translate = read_json(sub_translate_path)
        if sub_translate:
            for k2,v2 in sub_translate.items():
                path = k + '/' + k2
                link2 = gen_link(path)
                name2 = pad_str(k2, v2)
                s2 = "- [%s](%s)" %(name2, link2)
                print(s2)
        



def get_all(path):
    for root, dirs, files in os.walk(path):
        return {'root': root, 'dirs': sorted(dirs), 'files': sorted(files)}
    
print(get_all(c_dir))

# def gen(path):
#     contents_file = open(path + '/README.md', 'w', encoding='utf-8')
#     translate_file = open(path + '/translate', 'r').read()
#     translate = eval(translate_file)
#     path_info = get_all(path)
#     file_list = [ i for i in path_info['files'] if i not in ['README.md', 'translate'] ]
#     if file_list:
#         for file in file_list:
#             cmd_link_name = file[:file.rfind('.')]
#             cmd_link = "- [%s](%s/blob/%s/%s/%s)\n" %(cmd_link_name, repo_url, branch_name, path, file)
#             contents_file.write(cmd_link)

#     for dir in path_info['dirs']:
#         dir_link_name = translate.get(dir, dir)
#         dir_link = "### [%s](%s/tree/%s/%s/%s)\n" %(dir_link_name, repo_url, branch_name, path, dir)
#         contents_file.write(dir_link)
#         dirs = get_all(path + '/' + dir)
#         for cmd_file in dirs['files']:
#             cmd_link_name = cmd_file[:cmd_file.rfind('.')]
#             cmd_link = "- [%s](%s/blob/%s/%s/%s/%s)\n" %(cmd_link_name, repo_url, branch_name, path, dir, cmd_file)
#             contents_file.write(cmd_link)

#     contents_file.close()


def main():
    # hh()
    pass
    


if __name__ == '__main__':
    main()
    
# if __name__ == '__main__':
#     for i in need:
#         gen(i)
