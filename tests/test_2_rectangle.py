from source.my_classes import *
import pytest

a = Rectangle(5, 6)


def test_1_name():
    assert a.name == 'Rectangle'


def test_2_angles():
    assert a.angles == 4


def test_3_area():
    assert a.area == 30


def test_4_perimeter():
    assert a.perimeter == 22


def test_5_add_square():
    b = Quadrate(10)
    assert a.add_square(b) == 130


def test_6_incorrect_input_1():
    with pytest.raises(AttributeError):
        assert Rectangle(5, '6')


def test_7_incorrect_input_2():
    with pytest.raises(AttributeError):
        b = GeometrFigure()
        assert a.add_square(b)
