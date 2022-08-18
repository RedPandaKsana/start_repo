from src.figure import Figure

class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, a, b):
        self.a = a
        self.b = b
        if a<=0 or b<=0:
            raise ValueError("Невозможно создать прямоугольник")
        if a==b:
            raise ValueError("Для создания квадрата используйте функцию 'square'")

    @property
    def perimeter(self):
        return (self.a+self.b)*2

    @property
    def area(self):
        return self.a*self.b
