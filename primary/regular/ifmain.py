# print("Always executed")
#
# if __name__ == "__main__":
#     print("Executed when invoked directly")
# else:
#     print("Executed when imported")

import testmodule

print(testmodule.myfunc())
print(testmodule.myfuncadd(5, 8))