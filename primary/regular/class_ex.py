class A:
    def __init__(self):
        print("Init of A")

    def func1(self):
        print("func1 of A")

    # def __add__(self, other):
    #     print("Added")


class B(A):
    def __init__(self):
        print("Init of B")

    def func1(self):
        super().func1()
        print("func1 of B")

    def func2(self):
        print("func2 of B")

class C(B, A):
    def __init__(self):
        print("Init of C")

    def func1(self):
        # super().func1()
        print("func1 of C")

    def func2(self):
        print("func2 of C")

    def func3(self):
        print("func3 of C")

# a = A()
c = C()
c.func1()
