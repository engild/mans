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

def gen_contents(dir_name):
    contents_file = open(dir_name + '/README.md', 'w', encoding='utf-8')
    translate_file = open(dir_name + '/translate', 'r').read()
    translate = eval(translate_file)
    dirs = get_all(dir_name)['dirs']
    dirs = [ dir_name + '/' + i for i in dirs]
    for dir in dirs:
        dir_name = dir[dir.find('/') + 1:]
        link_name = translate.get(dir_name, dir_name)
        dir_link = "### [%s](%s/tree/%s/%s)\n" %(link_name, repo_url, branch_name, dir)
        contents_file.write(dir_link)
        for cmd_file in get_all(dir)['files']:
            cmd_link_name = cmd_file[:cmd_file.rfind('.')]
            cmd_link = "- [%s](%s/blob/%s/%s/%s)\n" %(cmd_link_name, repo_url, branch_name, dir, cmd_file)
            contents_file.write(cmd_link)

    contents_file.close()


if __name__ == '__main__':
    for i in need:
        gen_contents(i)
