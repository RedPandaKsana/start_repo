import math
from src.figure import Figure

class Triangle(Figure):
    name="Triangle"

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a<=0 or b<=0 or c<=0 or (a+b)<=c or (b+c)<=a or (a+c)<=b:
            raise ValueError("Невозможно создать треугольник!")

    @property
    def perimeter(self):
        return (self.a+self.b+self.c)/2

    @property
    def area(self):
        return math.sqrt((self.a+self.b+self.c)/2*((self.a+self.b+self.c)/2-self.a)*((self.a+self.b+self.c)/2-self.b)*((self.a+self.b+self.c)/2-self.c))
