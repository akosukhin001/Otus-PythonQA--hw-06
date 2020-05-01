from source.my_classes import *

a = Quadrate(8)


def test_1_name():
    assert a.name == 'Quadrate'


def test_2_angles():
    assert a.angles == 4


def test_3_area():
    assert a.area == 64


def test_4_perimeter():
    assert a.perimeter == 32


def test_5_add_square():
    b = Quadrate(10)
    assert a.add_square(b) == 164


def test_6_incorrect_input_1():
    c = Quadrate('6')
    assert None


def test_7_incorrect_input_2():
    b = GeometrFigure()
    assert a.add_square(b) == None
