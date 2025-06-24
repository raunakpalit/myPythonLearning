# class fibonacci:
#     def __init__(self, max= 10000):
#         self.a = 0
#         self.b = 1
#         self.max = max
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.a > self.max:
#             raise StopIteration
#
#         value_to_be_returned = self.a
#
#         self.a, self.b = self.b, self.a + self.b
#
#         return value_to_be_returned
#
# my_fibonacci_series = fibonacci(12)
# mfs = iter(my_fibonacci_series)
#
# print(next(mfs))
# print(next(mfs))
# print(next(mfs))
# print(next(mfs))
# print(next(mfs))


class Fibonacci:
    def __init__(self, max= 10000):
        self.a, self.b = 0, 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max:
            raise StopIteration
        value_to_be_returned = self.a
        self.a, self.b = self.b, self.a + self.b
        return value_to_be_returned

myfs = Fibonacci(12)
# for i in myfs:
#     print(i)

mfs = iter(myfs)
# print(next(mfs))
# print(next(mfs))
# print(next(mfs))
# print(next(mfs))
# print(next(mfs))
# print(next(mfs))
# print(next(mfs))
# print(next(mfs))


class Fibonacci:
    def __init__(self, max=10000):
        self.a, self.b = 0, 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.a < self.max:
            value_to_be_returned = self.a
            self.a, self.b = self.b, self.a + self.b
            return value_to_be_returned

f = Fibonacci(12)
mf = iter(f)
print(next(mf))
print(next(mf))
print(next(mf))
print(next(mf))
print(next(mf))
print(next(mf))
print(next(mf))
print(next(mf))
print(next(mf))


