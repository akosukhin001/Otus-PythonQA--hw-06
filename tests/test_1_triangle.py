from source.my_classes import *

a = Triangle(5, 7, 10)


def test_1_name():
    assert a.name == 'Triangle'


def test_2_angles():
    assert a.angles == 3


def test_3_area():
    assert a.area == 16.25


def test_4_perimeter():
    assert a.perimeter == 22


def test_5_add_square():
    b = Quadrate(10)
    assert a.add_square(b) == 116.25


def test_6_incorrect_input_1():
    c = Triangle(5, 5, 10)
    assert None


def test_7_incorrect_input_2():
    c = Triangle(5, 7, '10')
    assert None


def test_8_incorrect_input_3():
    b = GeometrFigure()
    assert a.add_square(b) == None
