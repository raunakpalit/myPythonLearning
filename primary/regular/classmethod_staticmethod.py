class A:
    name = 'This is class A'
    def __init__(self):
        print("Init of A")

    def func1(self):
        print("func1 of A")

    @classmethod
    def func2(cls):
        cls.name = 'Modified'

    @staticmethod
    def func3():
        print("This is a static method")

a = A()
print(a.name)
a.func2()
print(a.name)
a.func3()

