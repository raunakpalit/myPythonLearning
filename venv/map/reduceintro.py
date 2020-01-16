import functools
import timeit

def sum_list(x, y: int):
    return x + y

addlist = [2, 3, 5, 12, 9]

result = functools.reduce(sum_list, addlist)
print(result)

print(sum(addlist))


