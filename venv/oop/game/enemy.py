"""
Challenge 1:
Create a new Vampyre class that is a subclass of Enemy.
Vampyres have 3 lives and 12 hit points of damage
You can create a new Python file for a Vampyre if you like, but I would suggest adding it to the existing enemy.py file

Test your class by creating one or two Vampyre instances and displaying their details.
Also inflict some damage to make sure the take_damage method works ok.
Also make sure trolls can also take damage, because we have not tested that yet


Challenge 2:
To help consolidate your understanding of Inheritance, we have got a challenge for you to try out
The challenge is to create a VampyreKing subclass of Vampyre
A VampyreKing is going to be incredibly powerful, and any points of damage will be divided by 4
VampyreKing objects will also start off with 140 hit points.

So extend Vampyre to create a VampyreKing class with those additional properties
Test the new class by creating a new VampyreKing object and checking that it does start with 
140 hit points and only takes a quarter of the damage inflicted.
"""

import random

class Enemy:

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True
    
    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -=1
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.alive = False

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.hit_points}".format(self)


class Troll(Enemy):
    
    def __init__(self, name):
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0.name}, {0.name} stomp you".format(self))


class Vampyre(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("****** {0.name} dodges*******".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampyreKing(Vampyre):
    
    def __init__(self, name):
        super().__init__(name=name)
        self.hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage // 4)

    

