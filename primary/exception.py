class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def checkinput(self):
        print("Inside decorator")
        def inner(self):
            print("Inside Inner")
            self.a = int(self.a)
            self.b = int(self.b)
        return inner

    @checkinput
    def add(self):
        print(self.a + self.b)

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        self.a / self.b

cal = Calculator(12, 6)
print(cal.add())

# def de(add):
#     def inner(a, b):
#         add(int(a), int(b))
#     return inner

# @de
# def add(a, b):
#     print(a + b)

# add('12', '6')