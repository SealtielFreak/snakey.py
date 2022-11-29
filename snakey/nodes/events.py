from numpy import *

from snakey import Vector2
from snakey.nodes.group import *

from typing import Callable


class Events:
    def __init__(self):
        self.__events = {}

    @property
    def events(self):
        return self.__events

    def event(self, func):
        self.__events[func.__name__] = func

