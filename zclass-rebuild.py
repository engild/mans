import os


server = "https://github.com"
author = "engild"
repo = "mans"
repo_url = "%s/%s/%s" %(server, author, repo)
branch_name = open('branch-name', 'r').read()


class GenContents(object):
    def __init__(self, *args):
        # super(ClassName, self).__init__(*args))
        pass
    
    def get_all(path):
        for root, dirs, files in os.walk(path):
            return {'root': root, 'dirs': sorted(dirs), 'files': sorted(files)}
    
    def gen_dir_link(dir):
        pass
    
    def gen_file_link(file):
        # cmd_link_name = file[:file.rfind('.')]
        # cmd_link = "- [%s](%s/blob/%s/%s/%s)\n" %(cmd_link_name, repo_url, branch_name, path, file)
        pass
    
    def write_link(text):
        pass
needs = [
    'Debian-family-system-commands',
    'Linux-system-common-commands', 
    # 'Redhat-family-system-commands',
    # 'services',
    ]
# GenContents(need)