# for i in range(1,20):
#     print("i is now {}".format(i))

number = "9,223,373,036,854,775,807"
# for i in range(0, len(number)):
#     print(number[i])
# for i in number:
#     print(i)

cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))