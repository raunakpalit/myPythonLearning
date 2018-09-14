# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == "spam":
#         continue
#     print("Buy {}".format(item))

# print("==================")

# for item in shopping_list:
#     if item == "spam":
#         break
#     print("Buy {}".format(item))

meal = ["egg", "bacon", "spam", "sausages"]
nasty_food_item = ''

for item in meal:
    if item == "spam":
        nasty_food_item = item
        break
else:
    print("I'l have a plate of that, please")

if nasty_food_item:
    print("Can't I have anything without spam in it")
