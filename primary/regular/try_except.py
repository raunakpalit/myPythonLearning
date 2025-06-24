# try:
#     x = int(input("Enter a number"))
# except ValueError:
#     print("Oops! Not a number..")

# def this_fails(n):
#     x = 10/n
#     return x
#
# try:
#     a = this_fails(2)
#     print(a)
# except ZeroDivisionError as err:
#     print("Not divisible by 0. {}".format(err))
# except TypeError as err:
#     print("Type error here. {}".format(err))
# except NameError as err:
#     print("Name error here. {}".format(err))
# else:
#     print("Executed else block")
# finally:
#     print("Executed finally block")


# Raise Exception
# x = -1
# if x < 0:
#     raise Exception("No numbers below 0")


# x = "hello"
#
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")

# try:
#     x = int(input("Enter your roll number: "))
#     if x<0:
#         raise ValueError()
# except ValueError():
#     print("Value Error Exception thrown! Value cannot be less than 0")


# print(issubclass(Exception, object))


# Raising Own Exceptions

class MyOwnException(Exception):
    pass

try:
    roll = int(input("Please enter your roll number"))
    if roll < 0:
        raise MyOwnException
except MyOwnException:
    print("My own exception. Value cannot be less than 0")