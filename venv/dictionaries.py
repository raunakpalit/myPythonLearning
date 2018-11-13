fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit", 
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit)
# del fruit["lemon"]
# fruit.clear()
# print(fruit)

# print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     # description = fruit.get(dict_key, "We do not have a " + dict_key)
#     # print(description)
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We do not have a {}".format(dict_key))

# for snack in fruit:
#     print(fruit[snack])

# print(fruit)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for i in ordered_keys:
#     print(i + " - " + fruit[i])

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

# for val in fruit.values():
#     print(val)

# print(fruit.keys())
# print(fruit.values())

# fruit_keys = fruit.keys()
# print(fruit_keys)

# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)

# print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))
