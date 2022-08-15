import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle

@pytest.fixture
def default_circle():
    circle = Circle(2)
    yield circle
    del circle

@pytest.fixture
def default_square():
    square = Square(2)
    yield square
    del square

@pytest.fixture
def default_triangle():
    triangle = Triangle(1, 1, 1)
    yield triangle
    del triangle

@pytest.fixture
def default_rectangle():
    rectangle = Rectangle(2, 1)
    yield rectangle
    del rectangle
