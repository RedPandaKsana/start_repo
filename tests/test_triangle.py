import pytest
import math

from src.triangle import Triangle

def test_triangle_init_wrong():
    with pytest.raises(ValueError):
        t = Triangle(0, 1, 1)

def test_triangle_init_wrong2():
    with pytest.raises(ValueError):
        t = Triangle(1, 0, 1)

def test_triangle_init_wrong3():
    with pytest.raises(ValueError):
        t = Triangle(1, 1, 0)

def test_triangle_init_wrong4():
    with pytest.raises(ValueError):
        t = Triangle(-1, 1, 1)

def test_triangle_init_wrong5():
    with pytest.raises(ValueError):
        t = Triangle(1, -1, 1)

def test_triangle_init_wrong6():
    with pytest.raises(ValueError):
        t = Triangle(1, 1, -1)

def test_triangle_init_wrong7():
    with pytest.raises(ValueError):
        t = Triangle(3, 1, 1)

def test_triangle_init_wrong8():
    with pytest.raises(ValueError):
        t = Triangle(1, 3, 1)

def test_triangle_init_wrong9():
    with pytest.raises(ValueError):
        t = Triangle(1, 1, 3)

def test_triangle_name(default_triangle):
    assert default_triangle.name == "Triangle"

def test_triangle_area(default_triangle):
    assert default_triangle.area == math.sqrt((default_triangle.a+default_triangle.b+default_triangle.c)/2*((default_triangle.a+default_triangle.b+default_triangle.c)/2-default_triangle.a)*((default_triangle.a+default_triangle.b+default_triangle.c)/2-default_triangle.b)*((default_triangle.a+default_triangle.b+default_triangle.c)/2-default_triangle.c))

def test_triangle_perimeter(default_triangle):
    assert default_triangle.perimeter == (default_triangle.a+default_triangle.b+default_triangle.c)/2

def test_triangle_add_area_circle(default_triangle, default_circle):
    assert default_triangle.add_area(default_circle) == default_triangle.area + default_circle.area

def test_triangle_add_area_rectangle(default_triangle, default_rectangle):
    assert default_triangle.add_area(default_rectangle) == default_triangle.area + default_rectangle.area

def test_triangle_add_area_square(default_triangle, default_square):
    assert default_triangle.add_area(default_square) == default_triangle.area + default_square.area

def test_triangle_add_area_triangle(default_triangle):
    assert default_triangle.add_area(default_triangle) == default_triangle.area + default_triangle.area