def sum_digits(n): # n = 1234
    str_n = str(n) # '1234'
    sum_n = 0
    for i in str_n:
        sum_n = sum_n + int(i)
    print(sum_n)

# def rec_sum_digits(n): # n = 1234
#     if n == 0:
#         return 0
#     return (n%10 + rec_sum_digits(n//10))

def rec_sum_digits(n): # n = 1234
    if n == 0:
        return 0
    return n%10 + rec_sum_digits(n//10)


print(rec_sum_digits(1234))
print(rec_sum_digits(123456789))

