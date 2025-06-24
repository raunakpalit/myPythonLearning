class A:
    def __init__(self):
        print("Inside Class A")

    # def __sub__(self, m):
    #     return "Added"

    def __str__(self):
        return "Class A str"

class B:
    def __init__(self):
        print("Inside Class B")

    def __str__(self):
        return "Class B str"

a = A()
b = B()
print(a+b)

