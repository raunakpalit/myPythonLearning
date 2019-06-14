class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Wee.. This is fun.")
        elif self.ratio == 1:
            print("Not ideal. But still I can fly")
        else:
            print("I will better take a walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8) 

    def walk(self):
        print("Waddle waddle waddle")

    def swim(self):
        print("Come on in. The water is lovely")

    def quack(self):
        print("Quack. Quack. Quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):
    
    def walk(self):
        print("Waddle waddle.. I waddle too")

    def swim(self):
        print("Come on in. The water is chilly this far south")

    def quack(self):
        print("Are you grin? The larf. I am penguin")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

if __name__ == '__main__':
    Donald = Duck()
    Donald.fly()
    # test_duck(Donald)
    # Perce = Penguin()
    # test_duck(Perce)
