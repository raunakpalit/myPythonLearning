# Remove duplicates
def remove_duplicates(ulist):
    print(ulist)
    for num in ulist:
        indices = [i for i in range(len(ulist)) if ulist[i] == num]
        for occr in indices:
            if not occr == indices[0]:
                del ulist[occr]
    print(ulist)

def interchange_first_last(ulist):
    ulist[0], ulist[-1] = ulist[-1], ulist[0]
    print(ulist)

def swap_two_elements(ulist, pos1, pos2):
    ulist[pos1], ulist[pos2] = ulist[pos2], ulist[pos1]
    print(ulist)

def reverse(ulist):
    mod_list = []
    len_ulist = len(ulist)
    for i in range(len_ulist):
        mod_list.append(ulist[len_ulist -1 -i])
    print(mod_list)


# remove_duplicates([2, 3, 3, 6, 5, 2, 9, 6])
# interchange_first_last([1, 2, 3, 4, 5, 6, 7, 8])
# swap_two_elements([1, 2, 3, 4, 5, 6, 7, 8], 2, 6)
reverse([1, 2, 3, 4, 5, 6, 7, 8])