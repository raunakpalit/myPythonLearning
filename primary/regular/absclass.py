from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def no_of_sides(self):
        pass