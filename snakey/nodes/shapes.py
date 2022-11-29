from dataclasses import dataclass

from typing import TypeVar, Generic

from numpy import array

from snakey import Vector2
from snakey.nodes.transformable import Transformable


@dataclass
class Rect:
    top: Vector2
    bottom: Vector2
    left: Vector2
    right: Vector2

    def __str__(self):
        return f"[{self.top}, {self.bottom}, {self.left}, {self.right}]"


class PolygonShape(Transformable):
    @property
    def count_vertices(self) -> int:
        return len(self.transform.vertices)


class RectangleShape(Transformable):
    def __init__(self, width: float, height: float):
        super().__init__([
            Vector2(0, 0),
            Vector2(0, 1 * height),
            Vector2(1 * width, 1 * height),
            Vector2(1 * width, 0),
        ])

        self.__rect = Rect(
            Vector2(0, 0),
            Vector2(0, 1 * height),
            Vector2(1 * width, 1 * height),
            Vector2(1 * width, 0),
        )

    @property
    def rect(self) -> Rect:
        return self.__rect