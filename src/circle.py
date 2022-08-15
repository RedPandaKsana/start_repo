import math
from src.figure import Figure

class Circle(Figure):
    name = "Circle"

    def __init__(self, r):
        self.r = r
        if r<=0:
            raise ValueError("Невозможно создать круг!")

    @property
    def perimeter(self):
        return 2*math.pi*self.r

    @property
    def area(self):
        return math.pi*(self.r*self.r)
