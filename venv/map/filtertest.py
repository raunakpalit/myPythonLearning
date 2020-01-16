import timeit

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

print("-" * 40)


def spamless_comp():
    meals = [meal for meal in menu if "spam" not in meal]
    # print(meals)
    return meals

print("-" * 40)

def not_spam(meal_list: list):
    return "spam" not in meal_list


def spamless_filter():
    spamless_meal = list(filter(not_spam, menu))
    # print(spamless_meal)
    return spamless_meal


if __name__ == "__main__":
    print(spamless_comp())
    print(spamless_filter())
    print(timeit.timeit(spamless_comp, number=100000))
    print(timeit.timeit(spamless_filter, number=100000))