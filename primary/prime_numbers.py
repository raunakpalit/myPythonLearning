# Write a program to list down all the prime numbers from 1 to 100

# def is_prime(n):
#     if n <= 1 or n == 4:
#         return False
#     for num in range(2, int(n/2)):
#         if n%num == 0:
#             return False
#     else:
#          return True


# def all_primes(sn, en):
#     prime_list = []
#     for num in range(sn, en+1):
#         if is_prime(num):
#             prime_list.append(num)
#     print(prime_list)
#     print(len(prime_list))

# def count_all_primes(sn, en):
#     count = 0
#     for num in range(sn, en+1):
#         if is_prime(num):
#             count += 1
#     print("Total prime numbers in the range {} to {} is {}".format(sn, en, count))


# all_primes(1, 101)
# count_all_primes(1, 101)

# def is_prime(n):
#     for i in range(2, n):
#         if n%i == 0:
#             print("{} is not a prime number".format(n))
#             break
#     else:
#         print("{} is a prime number".format(n))

# is_prime(96)

def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            break
    else:
        print("{} is a prime number".format(n))

# is_prime(9)
prime_list_100 = [is_prime(num) for num in range(2, 100)]

            
