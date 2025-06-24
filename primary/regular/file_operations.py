import os

with open("file_ops.txt", "w+") as fo:
    fo.write("My name is Raunak Palit.\nI Have joined Wipro on 17th April 2023."
             "\nMy age is 34 and \nI am married to Monika.\nWe have a beautiful son Avyukt.\n")

try:
    with open("file_ops.txt", "r") as fr:
        print(fr.read())
except FileNotFoundError:
    print("File not found")

try:
    with open("file_ops.txt", "a+") as fa:
        fa.write("We love to call our son Leo.\nHe is 9 months old now.\n")
except IOError:
    print("File not found")

try:
    with open("file_ops.txt", "r") as fr:
        print(fr.read())
except FileNotFoundError:
    print("File not found")


# cwd = os.getcwd()
# print(cwd)
#
# print(os.path.exists("C:\\Codes\\venvName"))
# print(os.listdir(cwd))
# os.chdir("Include")
# print(os.getcwd())
# for i in os.walk(cwd):
#     print(i)
