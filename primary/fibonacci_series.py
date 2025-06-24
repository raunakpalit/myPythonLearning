# def fib_series(n):
#     series = [0, 1]
#     for i in range(2, n):
#         series.append(series[i -1] + series[i -2])
#     print(series)

# # fib_series(14)


# def rec_fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return rec_fib(n-1) + rec_fib(n-2)

# # for i in range(14):
# #     print(rec_fib(i))

# def fib_generator(n):
#     a, b = 0, 1
#     while n > 0:
#         yield a
#         a, b = b, a+b
#         n -=1

# f = fib_generator(12)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# fib_list = [0, 1]
# def fib_series(n):
#     while len(fib_list) < n:
#         fib_list.append(fib_list[-1] + fib_list[-2])

# fib_series(20)
# print(fib_list)

# def rec_fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return rec_fib(n-1) + rec_fib(n-2)

# for i in range(20):
#     print(rec_fib(i))


# def generate_fib(n):
#     a, b = 0, 1
#     while n > 0:
#         yield a
#         a, b = b, a+b
#         n -=1

# f = generate_fib(20)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# def fib_rec(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib_rec(n-1) + fib_rec(n-2)

# for i in range(20):
#     print(fib_rec(i))

def fib(n):
    series = [0, 1]
    while len(series) != 20:
        series.append(series[-1] + series[-2])
    return series

# print(fib(20))

def fib_for(n):
    series = [0, 1]
    for i in range(n-2):
        series.append(series[-1] + series[-2])
    return series

# print(fib_for(20))

def fib_iter(n):
    a, b = 0, 1
    while n > 0:
        yield a
        a, b = b, a+b
        n -=1


def rec_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return rec_fib(n-1) + rec_fib(n-2)
        






