from source.my_classes import *
import pytest

a = Circle(5)


def test_1_name():
    assert a.name == 'Circle'


def test_2_angles():
    assert a.angles == "No angles at all, I'm a circle!!"


def test_3_area():
    assert a.area == 78.5


def test_4_perimeter():
    assert a.perimeter == 31.4


def test_5_add_square():
    b = Quadrate(10)
    assert a.add_square(b) == 178.5


def test_6_incorrect_input_1():
    with pytest.raises(AttributeError):
        assert Circle('abcd')


def test_7_incorrect_input_2():
    with pytest.raises(AttributeError):
        # b = Circle(5)
        b = GeometrFigure()
        assert a.add_square(b)
