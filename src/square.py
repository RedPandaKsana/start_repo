from src.figure import Figure

class Square(Figure):
    name = "Square"

    def __init__(self, a):
        self.a = a
        if a<=0:
            raise ValueError("Невозможно создать квадрат!")

    @property
    def perimeter(self):
        return self.a*4

    @property
    def area(self):
        return self.a*self.a