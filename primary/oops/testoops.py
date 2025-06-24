class A:
    def __init__(self, name, id):
        print("Init of class A")
        self.name = name
        self.id = id

    def func1(self):
        print("This is func1 of class A")

    def func2(self):
        print("This is func2 of class A")


class B(A):
    def __init__(self, surname, childname):
        # super().__init__()
        self.surname = surname
        self.childname = childname
        print("Init of class B")
        # print(self.name)

    def func3(self):
        print("This is func3 of class B")

    def func4(self):
        print("This is func4 of class B")

    def master_print(self):
        print(self.name)


class C(B, A):
    def __init__(self):
        super().__init__()
        print("Init of class C")

    def func5(self):
        print("This is func3 of class C")

    def func6(self):
        print("This is func4 of class C")

# a = A()
# a.func1()
# a.func2()
b = B('Palit', 'Avyukt')
# b.func1()
# b.master_print()
# c = C()