mylist = ["{}: Even".format(x) if x%2 == 0 else "{}: Odd".format(x) for x in range(10)]
print(mylist)