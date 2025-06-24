class Animal:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def voice(self):
        return "I have a voice"

    def eat(self):
        return "I can eat"

    def movement(self):
        return "I can run"

    def no_of_legs(self):
        return "I have legs"


class Dog(Animal):
    def voice(self):
        return "Bark"
    
    def no_of_legs(self):
        return "I have 4 legs"

    def canine(self):
        return "I am of type canine"


class Cat(Animal):
    def voice(self):
        return "Meow"




a = Animal("Raunak", "1")
b = Animal("Santhosh", "2")