import shelve

with shelve.open('ShelfTest') as fruit:
    # fruit['orange'] = "a sweet, orange, citrus fruit"
    # fruit['apple'] = "good for making cider"
    # fruit['lemon'] = "a sour, yellow citrus fruit"
    # fruit['grape'] = "a small, sweet fruit growing in bunches"
    # fruit['lime'] = "a sour, green citrus fruit"

    # print(fruit["lemon"])
    # print(fruit["grape"])
    # fruit['lime'] = "great with tequila"
    # for snack in fruit:
    #     print(snack + ": " + fruit[snack])
# print(fruit)

    # while True:
    #     shelve_key = input("Please enter a fruit: ")
    #     if shelve_key == "quit":
    #         break
    #     description = fruit.get(shelve_key, "We don't have a " + shelve_key)
    #     print(description)

    # for f in fruit:
    #     print(f + " - " + fruit[f])

    for v in fruit.values():
        print(v)
    print(fruit.values())

    for i in fruit.items():
        print(i)
    print(fruit.items())