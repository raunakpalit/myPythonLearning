import os

root = "test"

for path, directories, files in os.walk(root, topdown=True):
    print(path)
    print(directories)
    print(files)
    print("*" * 40)