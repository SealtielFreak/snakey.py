from snakey.nodes.node import *
from snakey.nodes.group import *
from snakey.nodes.transform import *
from snakey.nodes.events import Events
from types import SimpleNamespace


class Scene(Node):
    def __init__(self):
        self.__events = {}
        self.__references = SimpleNamespace()
        self.root = Group()

    @property
    def references(self):
        return self.__references

    @property
    def events(self):
        return self.__events

    def action(self, func):
        arg_count = lambda f: f.__code__.co_argcount
        name = func.__name__

        if arg_count(func) == 2:
            self.__events[name] = lambda group, ref: func(group, ref)
        elif arg_count(func) == 1:
            self.__events[name] = lambda group, ref: func(group)
        elif arg_count(func) == 0:
            self.__events[name] = lambda group, ref: func()
        else:
            raise "Invalid function"
