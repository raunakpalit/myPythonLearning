import os

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

print(parent_dir)

jenkinsfilepath = "{}/Jenkinsfile".format(parent_dir)
readmepath = "{}/README.md".format(parent_dir)
testfilepath = "{}/test.py".format(parent_dir)

print("Jenkinsfile exists: {}".format(os.path.exists(jenkinsfilepath)))
print("Readme exists: {}".format(os.path.exists(readmepath)))
print("test exists: {}".format(os.path.exists(testfilepath)))