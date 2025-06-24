class Alphabet:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        print("Getting value")
        return self._value

    @value.setter
    def value(self, value):
        print("Setting value")
        self._value = value

    @value.deleter
    def value(selfs):
        print("Deleting value")
        del self._value

x = Alphabet("Raunak")
print(x.value)
x.value = "Palit"
print(x.value)