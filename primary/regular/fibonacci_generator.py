def fibonacci(n):
    count = 0
    a, b = 0, 1
    while count < n:
        yield a
        count += 1
        a, b = b, a+b

f = fibonacci(12)
for i in f:
    print(i)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))