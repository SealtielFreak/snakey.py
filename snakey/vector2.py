from numpy import *


class Vector2:
    def __init__(self, *args):
        n_vec2 = lambda x, y: array([x, y], dtype="float64")
        l_args = len(args)

        if l_args == 2:
            self.__vec = n_vec2(*args)
        elif l_args == 1:
            self.__vec = n_vec2(*args[0])
        elif l_args == 0:
            self.__vec = n_vec2(0, 0)
        else:
            raise "Invalid argument"

    @property
    def array(self) -> array:
        return self.__vec

    @property
    def x(self) -> float:
        return self.__vec[0]

    @property
    def y(self) -> float:
        return self.__vec[1]

    @x.setter
    def x(self, x):
        self.__vec[0] += x

    @y.setter
    def y(self, y):
        self.__vec[1] += y

    def __iter__(self):
        return iter(self.__vec)

    def __getitem__(self, item: int) -> float:
        return self.__vec[item]

    def __add__(self, other):
        return Vector2(self.__vec + other) if not type(other) is Vector2 else Vector2(self.__vec + other.__vec)

    def __sub__(self, other):
        return Vector2(self.__vec - other) if not type(other) is Vector2 else Vector2(self.__vec - other.__vec)

    def __mul__(self, other):
        return Vector2(self.__vec * other) if not type(other) is Vector2 else Vector2(self.__vec * other.__vec)

    def __truediv__(self, other):
        return Vector2(self.__vec / other) if not type(other) is Vector2 else Vector2(self.__vec / other.__vec)

    def __str__(self):
        return str(self.__vec)