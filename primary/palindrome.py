# def reverse_int(n):
#     num = 0
#     while n != 0:
#         den = n % 10 # d = 1, d = 2
#         n = n//10 # n = 1234432, n = 123443
#         num = num*10 + den #  num = 1, 12
#     return num

# def int_is_palindrome(n):
#     if n == reverse_int(n):
#         print("Number is a palindrome")
#     else:
#         print("Not a palindrome")


# def reverse_str(istr):
#     rev_str = ''
#     str_len = len(istr) # 5
#     for i in range(str_len):
#         rev_str = rev_str + istr[str_len - i -1]
#     return rev_str

# def str_is_palindrome(istr):
#     if istr == reverse_str(istr):
#         print("{} is palindrome".format(istr))
#     else:
#         print("{} is not a palindrome".format(istr))

# int_is_palindrome(12344321)
# int_is_palindrome(1234321)
# int_is_palindrome(12354321)
# int_is_palindrome(12345321)
# str_is_palindrome("naman")
# str_is_palindrome("malayalam")
# str_is_palindrome("raunak")
# str_is_palindrome("monika")

# def is_palindrome(n):
#     if "int" in str(type(n)):
#         n = str(n)
#     else:
#         n = n.lower()
#     if n == n[::-1]:
#         print("{} is a palindrome".format(n))
#     else:
#         print("{} is not a palindrome".format(n))

# def reverse_str(istr):
#     rev_str = ""
#     str_len = len(istr)
#     while str_len !=0:
#         rev_str = rev_str + istr[str_len -1]
#         str_len -=1
#     return rev_str

# print(reverse_str("raunak"))


def rev_int(n): # n = 123456
    num = 0
    while n !=0:
        den = n%10 #6, 5
        n = n//10 # 12345, 1234
        num = num*10 + den # 6, 65
    return num

print(rev_int(32123456))

# is_palindrome("Raunak")
# is_palindrome("Nishit")
# is_palindrome("Naman")
# is_palindrome("Malayalam")
# is_palindrome("123321")
# is_palindrome(123443211123)


