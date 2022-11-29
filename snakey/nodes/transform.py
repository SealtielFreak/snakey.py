import math


from numpy.typing import NDArray
from numpy import array

from snakey import Vector2


class Transform:
    def __init__(self, vertices: NDArray[Vector2]):
        self.__vertices = array([Vector2(vec) for vec in vertices])

    @property
    def vertices(self) -> NDArray[Vector2]:
        return self.__vertices

    def __str__(self):
        return str([[*vec] for vec in self.vertices])

    def translate(self, offset: Vector2):
        self.__vertices += offset

    def rotate(self, angle: float, origin: Vector2 = Vector2([0, 0])):
        self.__fix_origin(origin)

        self.__vertices = [Vector2(
            vec.x * math.cos(angle) - vec.y * math.sin(angle) + origin.x,
            vec.x * math.sin(angle) + vec.y * math.cos(angle) + origin.y
        ) for vec in self.vertices]

    def scale(self, scale: Vector2, offset: Vector2 = Vector2([0, 0])):
        self.__fix_origin(offset)

        self.__vertices = [Vector2(
            (vec.x * scale.x) + offset.x,
            (vec.y * scale.y) + offset.y
        ) for vec in self.vertices]

    def __fix_origin(self, origin: Vector2):
        self.__vertices = map(lambda v: v - origin, self.vertices)
