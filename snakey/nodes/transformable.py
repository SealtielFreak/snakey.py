from numpy.typing import NDArray
import numpy

from typing import Callable

from snakey import Vector2
from snakey.nodes import Transform
from snakey.nodes.node import Node


class Transformable(Node):
    def __init__(self, vertices: NDArray[Vector2]):
        self.__transform = Transform(vertices=vertices)
        self.__angle = 0
        self.__position = Vector2()
        self.__origin = Vector2()

    @property
    def origin(self) -> Vector2:
        return self.__origin

    @origin.setter
    def origin(self, origin: Vector2):
        self.__origin = origin

    @property
    def transform(self) -> Transform:
        return self.__transform

    @property
    def position(self) -> Vector2:
        return self.__position

    @position.setter
    def position(self, position: Vector2):
        move = position - self.position
        self.__position = position
        self.__origin += move
        self.transform.translate(move)

    @property
    def angle(self) -> float:
        return self.__angle

    @angle.setter
    def angle(self, angle: float):
        rotate = angle - self.__angle
        self.__angle = angle
        self.transform.rotate(rotate)


def translate(offset: Vector2) -> Callable[[Transformable], Transformable]:
    def inner(transformable):
        transformable.position += offset
        return transformable

    return inner


def rotate(angle: float) -> Callable[[Transformable], Transformable]:
    def inner(transformable):
        transformable.transform.rotate(angle, transformable.origin)
        return transformable

    return inner


def mid_vertices(vertices: NDArray[Vector2]) -> Vector2:
    return numpy.sum(vertices) / len(vertices)