"""
Input= {'All': [1, 2, 3], 'is': [1, 4], 'well': [4, 2]}
Output= {1: ['All', 'is'], 2: ['All', 'well'], 3: ['All'], 4: ['is', 'well']}
"""


# idict = {'All': [1, 2, 3], 'is': [1, 4], 'well': [4, 2]}

# odict = {}
# for i in idict.items():
#     for j in i[1]:
#         if j not in odict:
#             odict[j] = [i[0]]
#         else:
#             odict[j].append(i[0])

# print(odict)

idict = {'All': [1, 2, 3], 'is': [1, 4], 'well': [4, 2]}

odict = {}
for i in idict.items():
    for j in i[1]:
        if j not in odict:
            odict[j] = [i[0]]
        else:
            odict[j].append(i[0])
print(odict)



