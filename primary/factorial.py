# def fact(n):
#     result = 1
#     for i in range(1, n+1):
#         result = result * i
#     print(result)

# def rec_fact(n):
#     if n == 1:
#         return n
#     return n * rec_fact(n-1)

# # fact(6)
# print(rec_fact(4))

# def fact(n):
#     result = 1
#     for i in range(1, n+1):
#         result = result * i
#     return result

# print(fact(5))

# def fact_rec(n):
#     if n == 1:
#         return 1
#     return n * fact_rec(n-1)
# print(fact_rec(5))

# def fact_rec(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact_rec(n-1)
# print(fact_rec(5))

# def fact(n):
#     outp = 1
#     while n != 0:
#         outp = outp * n
#         n -=1
#     return outp

# print(fact(8))

# def fact_1(n):
#     result = 1
#     for i in range(2, n+1):
#         result = result * i
#     return result

# print(fact_1(8))

def rec_fact(n):
    if n == 0 or n == 1:
        return 1
    return n * rec_fact(n-1)

print(rec_fact(4))
print(rec_fact(8))