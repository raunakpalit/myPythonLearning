from absclass import Polygon

class Triangle(Polygon):
    def no_of_sides(self):
        print("I have 3 sides")

class Rectangle(Polygon):
    def no_of_sides(self):
        print("I have 4 sides")

class Pentagon(Polygon):
    def no_of_sides(self):
        print("I have 5 sides")

p = Pentagon()
# p.no_of_sides()