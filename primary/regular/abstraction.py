from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Human(Animal):
    def speak(self):
        print("I can talk")

class Dog(Animal):
    def speak(self):
        print("I can bark")

class Snake(Animal):
    def speak(self):
        print("I can hiss")

    def move(self):
        print("I can crawl")

s = Snake()
s.move()
# s.speak()