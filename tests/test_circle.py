import pytest
import math

from src.circle import Circle

def test_circle_init_wrong():
    with pytest.raises(ValueError):
        c = Circle(0)

def test_circle_init_wrong2():
    with pytest.raises(ValueError):
        c = Circle(-1)

def test_circle_name(default_circle):
    assert default_circle.name == "Circle"

def test_circle_area(default_circle):
    assert default_circle.area == math.pi*(default_circle.r*default_circle.r)

def test_circle_perimeter(default_circle):
    assert default_circle.perimeter == 2*math.pi*default_circle.r

def test_circle_add_area_square(default_circle, default_square):
    assert default_circle.add_area(default_square) == default_circle.area+default_square.area

def test_circle_add_area_triangle(default_circle, default_triangle):
    assert default_circle.add_area(default_triangle) == default_circle.area+default_triangle.area

def test_circle_add_area_rectangle(default_circle, default_rectangle):
    assert default_circle.add_area(default_rectangle) == default_circle.area+default_rectangle.area

def test_circle_add_area_circle(default_circle):
    assert default_circle.add_area(default_circle) == default_circle.area+default_circle.area

def test_circle_add_area_wrong(default_circle):
    a = 1
    with pytest.raises(ValueError):
        default_circle.add_area(a)