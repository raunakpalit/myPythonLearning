class Vehicle:
    COLOR = 'White'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = None

    def get_max_speed(self):
        return self.max_speed

    def get_mileage(self):
        return self.mileage

    def seating_capacity(self, capacity):
        self.capacity = capacity
        return "The seating capacity of the {} is {}".format(self.name, capacity)

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

    def fare(self):
        total_fare = self.capacity * 100
        return total_fare + (0.1 * total_fare)

class Car(Vehicle):
    def seating_capacity(self, capacity=4):
        return super().seating_capacity(capacity)

myvehicle = Bus('Volvo', 200, 10)
mycar = Car('i20', 170, 11)

myvehicle.seating_capacity()
mycar.seating_capacity()

print(myvehicle.fare())
print(mycar.fare())

print(type(myvehicle))
print(type(mycar))

print(isinstance(myvehicle, Vehicle))
# print("Color: {}, Vehicle Name: {}, Speed: {}, Mileage: {}"
#       .format(myvehicle.COLOR, myvehicle.name, myvehicle.max_speed, myvehicle.mileage))

# print("Color: {}, Vehicle Name: {}, Speed: {}, Mileage: {}"
#       .format(mycar.COLOR, mycar.name, mycar.max_speed, mycar.mileage))

# print(myvehicle.name)
# print(myvehicle.get_max_speed())
# print(myvehicle.get_mileage())