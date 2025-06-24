class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return "Person Details: \nName: {}\nAge: {}".format(self.name, self.age)

    def __repr__(self):
        return "{} {}".format(self.name, self.age)

a = Human("Raunak", 36)
print(a)