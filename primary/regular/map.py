# my_list = [x*x for x in range(5) if x%2==0]
# print(my_list)

# square = map(lambda x: x*x if(x%2==0) else None, range(5))
# for i in square:
#     print(i)

my_list = map(lambda x: x*x if (x%2==0) else None, range(5))
for i in my_list:
    print(i)