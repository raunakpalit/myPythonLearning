def insertion_sort(ulist):
    len_ulist = len(ulist)
    for i in range(1, len_ulist):
        key = ulist[i] #key = 1
        # print("Key is: {}".format(key))
        j= i -1 # j=0
        while j >= 0 and key < ulist[j]:
            ulist[j + 1] = ulist[j]
            j -=1
        ulist[j+1] = key
    print(ulist)

insertion_sort([3, 1, 6, 9, 2, 12, 98, 53, 42, 49])

