import os
import subprocess

curr_dir = os.getcwd()
dire = 'Include'

path = os.path.join(curr_dir, dire)
# print(path)
#
# print(os.path.exists(path))
# print(os.name)
# print(os.popen('dir').read())
print(subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE).stdout.read())
