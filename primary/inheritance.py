class A:
    def __init__(self):
        pass

    def method_1(self):
        print("Method 1 of class A")

class B(A):
    def __init__(self):
        pass

    def method_2(self):
        print("Method 2 of class B")

class C(B):
    def __init__(self):
        pass

    def method_1(self):
        print("Method 1 of class C")


obj_c = C()
print(dir(obj_c))
