from snakey import Vector2
from snakey.nodes.node import *
from snakey.nodes.transform import *


class Group(Node, Transform):
    def __init__(self, *childs) -> None:
        self.__position = Vector2(0, 0)
        self.__childs = [*childs]

    def __class_getitem__(cls, *args):
        if len(args) > 1:
            args = args[0]

        return Group(*args)

    def __iter__(self):
        return iter(self.__childs)

    @property
    def position(self) -> array:
        return self.__position

    @position.setter
    def position(self, position: array):
        move = self.translate(position - self.position)
        self.__position = position

        [child | move for child in self]

    def __xor__(self, *childs):
        childs = childs if not type(childs[0]) == tuple else childs[0]

        [self.__childs.append(child) for child in childs]
