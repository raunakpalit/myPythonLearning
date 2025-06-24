class PrimeNumber:
    '''Prime numbers'''
    def __init__(self, max=100):
        self.a = 1
        self.max = max

    def is_prime(self, n):
        for num in range(2, n):
            if n%num == 0:
                return False
        else:
            return True

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max:
            raise StopIteration

        value = None

        if self.is_prime(self.a):
            # print("{} is a prime number".format(self.a))
            value = self.a
        self.a = self.a + 1
        return value


# print(help(PrimeNumber))
prnm = PrimeNumber(10)
# # print(prnm)
# # for i in prnm:
# #     print(i)
# pm = iter(prnm)
# print(next(pm))
# print(next(pm))
# print(next(pm))
# print(next(pm))
# print(next(pm))
# print(next(pm))
# print(next(pm))
# print(next(pm))
# print(next(pm))
# print(next(pm))


