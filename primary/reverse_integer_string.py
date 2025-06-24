# Write a function to reverse the integer or string

def reverse_integer(n):
    new_num = 0
    while n != 0: #n = 321, n = 32, n = 2
        den = n%10 # den = 1, den = 2, den = 3
        n = n//10 # n = 32, n = 2, n = 0
        new_num = new_num*10 + den # new_n = 1, new_n = 12, new_n = 123
    print(new_num)


# reverse_integer(321432543)


def reverse_string(istr):
    c_set = ''
    for c in range(0, len(istr)): # 0, 1, 2, 3, 4, 5
        character = istr[-1 - c]
        c_set = c_set + character
    print(c_set)


reverse_string('Raunak')