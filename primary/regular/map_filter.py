n = [1, 2, 4, 5, 9]

map_squares = map(lambda x:x*x, n)
for i in map_squares:
    print(i)

list_squares = [x*x for x in n]
print(list_squares)