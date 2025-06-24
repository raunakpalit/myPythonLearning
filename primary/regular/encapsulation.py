class A:
    def __init__(self):
        self.x = 4
        self._y = 5
        self.__z = 6
        # print(self.x)
        # print(self._y)
        # print(self.__z)

    def func1(self):
        print("x is: {}".format(self.x))
        print("y is: {}".format(self._y))
        print("z is: {}".format(self.__z))

class B(A):
    def __init__(self):
        A.__init__(self)
        print(self.x)
        self.x = 7
        self._y = 8
        # print(self.__z)
        print(self.x)
        print(self._y)

    def func2(self):
        print("x is: {}".format(self.x))
        print("y is: {}".format(self._y))
        print("z is: {}".format(self.__z))

# b = B()
a = A()
print(a.x)
print(a._y)
# print(a.__z)
# b.func2()
print(a._A__z)
