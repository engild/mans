import os


server = "https://github.com"
author = "engild"
repo = "mans"
repo_url = "%s/%s/%s" %(server, author, repo)
branch_name = open('branch-name', 'r').read()

need = [
    'Debian-family-system-commands',
    'Linux-system-common-commands', 
    'Redhat-family-system-commands',
    'services',
    ]


def get_all(path):
    for root, dirs, files in os.walk(path):
        return {'root': root, 'dirs': sorted(dirs), 'files': sorted(files)}

def gen(path):
    contents_file = open(path + '/README.md', 'w', encoding='utf-8')
    translate_file = open(path + '/translate', 'r').read()
    translate = eval(translate_file)
    path_info = get_all(path)
    file_list = [ i for i in path_info['files'] if i not in ['README.md', 'translate'] ]
    if file_list:
        for file in file_list:
            cmd_link_name = file[:file.rfind('.')]
            cmd_link = "- [%s](%s/blob/%s/%s/%s)\n" %(cmd_link_name, repo_url, branch_name, path, file)
            contents_file.write(cmd_link)

    for dir in path_info['dirs']:
        dir_link_name = translate.get(dir, dir)
        dir_link = "### [%s](%s/tree/%s/%s/%s)\n" %(dir_link_name, repo_url, branch_name, path, dir)
        contents_file.write(dir_link)
        dirs = get_all(path + '/' + dir)
        for cmd_file in dirs['files']:
            cmd_link_name = cmd_file[:cmd_file.rfind('.')]
            cmd_link = "- [%s](%s/blob/%s/%s/%s/%s)\n" %(cmd_link_name, repo_url, branch_name, path, dir, cmd_file)
            contents_file.write(cmd_link)

    contents_file.close()


if __name__ == '__main__':
    for i in need:
        gen(i)
