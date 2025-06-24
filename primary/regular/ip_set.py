# List comprehensions to create a list for ipv4 random numbers example 192.10.23.54
# like these ip 5 nos

import random

# generate_random_ip = str(random.randint(100, 200)) + "." + str(random.randint(0, 100)) +\
#                      "." + str(random.randint(0, 100)) + "." +str(random.randint(0, 100))
# print(generate_random_ip)

ip_list = [str(random.randint(100, 200)) + "." + str(random.randint(0, 100)) +\
                     "." + str(random.randint(0, 100)) + "." +str(random.randint(0, 100)) for i in range(5)]

print(ip_list)


