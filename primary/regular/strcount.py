a = 'aaasaddjiexccadwds'
ostr = ''
# o/p = 'a'
# for i in a:
#     if i not in ostr:
#         ostr += i
#         ct = str(a.count(i))
#         ostr += ct
# print(ostr)
for i in a:
    if i in ostr:
        continue
    else:
        ostr += i
        ct = str(a.count(i))
        ostr += ct
print(ostr)