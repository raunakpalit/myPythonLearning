class Animal:
    def __init__(self, name):
        self.name = name

    def voice(self):
        print("Animal Voice")

    def eat(self):
        print("I can eat")

    def movement(self):
        print("I can run")

class Dog(Animal):
    def voice(self):
        print("I am a dog. My name is {} and I bark!".format(self.name))

class Cat(Animal):
    def voice(self):
        print("I am a cat. My name is {} and I meow!".format(self.name))

class Horse(Animal):
    def voice(self):
        print("I am a horse. My name is {} and I neigh!".format(self.name))


lab = Dog("Mikey")
lab.voice()
lab.eat()

# mycat = Cat("Munchi")
# mycat.voice()
# mycat.eat()
#
# myhorse = Horse("Chetak")
# myhorse.voice()
# myhorse.movement()