import os

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

print(parent_dir)

jenkinsfilepath = "{}/Jenkinsfile".format(parent_dir)
readmepath = "{}/README.md".format(parent_dir)
testfilepath = "{}/projectTest/test.py".format(parent_dir)
randompath = "{}/projectTest/xyz.py".format(parent_dir)

print("Jenkinsfile exists: {}".format(os.path.exists(jenkinsfilepath)))
print("Readme exists: {}".format(os.path.exists(readmepath)))
print("test exists: {}".format(os.path.exists(testfilepath)))
print("random exists: {}".format(os.path.exists(randompath)))
