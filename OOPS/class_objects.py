class A:
    def __init__(self):
        print("Init of Class A")
    
    def feature1(self):
        print("Feature 1 of Class A")

    def feature2(self):
        print("Feature 2 of Class A")

class B():
    def __init__(self):
        print("Init of Class B")
    
    def feature3(self):
        print("Feature 3 of Class B")

    def feature4(self):
        print("Feature 4 of Class B")

    def feature7(self):
        super().feature1()


class C(A, B):
    def __init__(self):
        super().__init__()
        print("Init of Class C")

    def feature5(self):
        print("Feature 5 of Class C")

    # def feature6(self):
    #     print("Feature 6 of Class C")


a = C()
