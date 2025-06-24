def bubble_sort(ulist):
    list_length = len(ulist)
    for i in range(list_length -1):
        for j in range(list_length -i -1):
            if ulist[j] > ulist[j + 1]:
                ulist[j], ulist[j + 1] = ulist[j + 1], ulist[j]

    print(ulist)


bubble_sort([3, 1, 6, 9, 2, 12, 98, 53, 42, 49])