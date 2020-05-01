import math

PI_VALUE = 3.14


class GeometrFigure():
    _angles = None
    _figure_name = None

    def __init__(self, len_a=None, len_b=None, len_c=None, radius=None):
        self.__figure_name = self._figure_name
        self.__angles_number = self._angles
        self.__len_a = len_a
        self.__len_b = len_b
        self.__len_c = len_c
        self._radius = radius
        self.my_vars = []

    @property
    def name(self):
        return self._figure_name

    @property
    def angles(self):
        return self.__angles_number

    @property
    def area(self):
        if self.__class__ == Quadrate:
            return round(self.__len_a ** 2, 2)
        elif self.__class__ == Rectangle:
            return round(self.__len_a * self.__len_b, 2)
        elif self.__class__ == Circle:
            return round(PI_VALUE * self._radius ** 2, 2)
        elif self.__class__ == Triangle:
            self.__half_perim = self.perimeter / 2
            p = self.__half_perim
            return round(math.sqrt(p * ((p - self.__len_a) * (p - self.__len_b) * (p - self.__len_c))), 2)

    @property
    def perimeter(self):
        if self.__class__ == Quadrate:
            return round(self.__len_a * 4, 2)
        elif self.__class__ == Rectangle:
            return round((self.__len_a + self.__len_b) * 2, 2)
        elif self.__class__ == Circle:
            return round(2 * PI_VALUE * self._radius, 2)
        elif self.__class__ == Triangle:
            return round(self.__len_a + self.__len_b + self.__len_c, 2)

    def arg_check(self):
        for var in self.my_vars:
            if type(var) not in [int, float]:
                raise AttributeError('Please use integer or float!')

    def add_square(self, other_figure):
        if type(other_figure) not in [Quadrate, Rectangle, Quadrate, Circle]:
            raise AttributeError('Please provide correct figure [Tringle, Rectangle, Quadrate or Circle]')
        else:
            print(self.area + other_figure.area)
            return self.area + other_figure.area


class Triangle(GeometrFigure):
    _angles = 3
    _figure_name = 'Triangle'

    def __init__(self, len_a, len_b, len_c):
        super().__init__(len_a, len_b, len_c)
        self.__figure_name = self._figure_name
        self.__angles_number = self._angles
        self.my_vars = [len_a, len_b, len_c]
        self.arg_check()
        if self.my_vars[0] >= self.my_vars[1] + self.my_vars[2]:
            raise AttributeError('Cannot build triangle using provided sides!')
        elif self.my_vars[1] >= self.my_vars[0] + self.my_vars[2]:
            raise AttributeError('Cannot build triangle using provided sides!')
        elif self.my_vars[2] >= self.my_vars[0] + self.my_vars[1]:
            raise AttributeError('Cannot build triangle using provided sides!')
        self.__len_a = len_a
        self.__len_b = len_b
        self.__len_c = len_c
        self.__half_perim = self.perimeter / 2


class Rectangle(GeometrFigure):
    _angles = 4
    _figure_name = 'Rectangle'

    def __init__(self, len_a, len_b):
        super().__init__(len_a, len_b)
        self.__figure_name = self._figure_name
        self.__angles_number = self._angles
        self.my_vars = [len_a, len_b]
        self.arg_check()
        self.__len_a = len_a
        self.__len_b = len_b


class Quadrate(GeometrFigure):
    _angles = 4
    _figure_name = 'Quadrate'

    def __init__(self, len_a):
        super().__init__(len_a)
        self.my_vars = [len_a]
        self.arg_check()
        self.__figure_name = self._figure_name
        self.__angles_number = self._angles
        self.__len_a = len_a


class Circle(GeometrFigure):
    _angles = 'No angles at all, I\'m a circle!!'
    _figure_name = 'Circle'

    def __init__(self, radius):
        super().__init__(radius)
        self.my_vars = [radius]
        self.arg_check()
        self.__figure_name = self._figure_name
        self.__angles_number = self._angles
        self._radius = radius
