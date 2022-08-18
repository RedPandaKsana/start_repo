import pytest
import math

from src.square import Square

def test_square_init_wrong():
    with pytest.raises(ValueError):
        s = Square(0)

def test_square_init_wrong2():
    with pytest.raises(ValueError):
        s = Square(-1)

def test_square_name(default_square):
    assert default_square.name == "Square"

def test_square_area(default_square):
    assert default_square.area == default_square.a * default_square.a

def test_square_perimeter(default_square):
    assert default_square.perimeter == default_square.a * 4

def test_square_add_area_circle(default_square, default_circle):
    assert default_square.add_area(default_circle) == default_square.area + default_circle.area

def test_square_add_area_rectangle(default_square, default_rectangle):
    assert default_square.add_area(default_rectangle) == default_square.area + default_rectangle.area

def test_square_add_area_triangle(default_square, default_triangle):
    assert default_square.add_area(default_triangle) == default_square.area + default_triangle.area

def test_square_add_area_square(default_square):
    assert default_square.add_area(default_square) == default_square.area + default_square.area

def test_square_add_area_wrong(default_square):
    a = 1
    with pytest.raises(ValueError):
        default_square.add_area(a)
