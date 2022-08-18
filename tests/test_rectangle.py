import pytest
import math

from src.rectangle import Rectangle

def test_rectangle_init_wrong():
    with pytest.raises(ValueError):
        r = Rectangle(1, 1)

def test_rectangle_init_wrong2():
    with pytest.raises(ValueError):
        r = Rectangle(0, 1)

def test_rectangle_init_wrong3():
    with pytest.raises(ValueError):
        r = Rectangle(1, 0)

def test_rectangle_init_wrong4():
    with pytest.raises(ValueError):
        r = Rectangle(0, 0)

def test_rectangle_init_wrong5():
    with pytest.raises(ValueError):
        r = Rectangle(-1, 1)

def test_rectangle_init_wrong6():
    with pytest.raises(ValueError):
        r = Rectangle(1, -1)

def test_rectangle_name(default_rectangle):
    assert default_rectangle.name == "Rectangle"

def test_rectangle_area(default_rectangle):
    assert default_rectangle.area == default_rectangle.a * default_rectangle.b

def test_rectangle_perimeter(default_rectangle):
    assert default_rectangle.perimeter == (default_rectangle.a + default_rectangle.b)*2

def test_rectangle_add_area_circle(default_rectangle, default_circle):
    assert default_rectangle.add_area(default_circle) == default_rectangle.area + default_circle.area

def test_rectangle_add_area_square(default_rectangle, default_square):
    assert default_rectangle.add_area(default_square) == default_rectangle.area + default_square.area

def test_rectangle_add_area_triangle(default_rectangle, default_triangle):
    assert default_rectangle.add_area(default_triangle) == default_rectangle.area + default_triangle.area

def test_rectangle_add_area_wrong(default_rectangle):
    a = 1
    with pytest.raises(ValueError):
        default_rectangle.add_area(a)