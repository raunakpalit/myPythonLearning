# With different data types
# istr = 'raunak'
# ilst = [1, 2, 3, 4]
#
# print(len(istr))
# print(len(ilst))

# With different arguments
# def add(*args):
#     return sum(*args)
#
# print(add((2, 3)))
# print(add((5, 6, 7, 8)))


# polymorphism in class
class India:
    def capital(self):
        print("Delhi")

    def language(self):
        print("Hindi")

class USA:
    def capital(self):
        print("Washington")

    def language(self):
        print("English")


i = India()
u = USA()
i.capital()
i.language()
u.capital()
u.language()


# With Inheritance -- method overriding
class Bird:
    def intro(self):
        print("I am a bird")

    def flight(self):
        print("Some can fly, some cannot")

class Sparrow(Bird):
    def flight(self):
        print("I can fly")

class Ostrich(Bird):
    def flight(self):
        print("I cannot fly")



