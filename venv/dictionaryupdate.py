fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can I have some more fruit, please"}

print(veg)

# veg.update(fruit)
# print(veg)

# print(fruit.update(veg))
# print(fruit)

nice_and_tasty = fruit.copy()
nice_and_tasty.update(veg)
print(nice_and_tasty)
print(veg)
print(fruit)