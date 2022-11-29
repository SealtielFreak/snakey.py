from dataclasses import dataclass
from ctypes import byref, c_void_p
from typing import Generator, Any, Dict, List

from sdl2 import *


class Events:
    @dataclass
    class Event:
        name: str
        common: Dict[str, str]

    def __init__(self) -> None:
        Events.__events_test = ""
        self.__event = SDL_Event()
        self.__events_name = {
            SDL_QUIT: "closed"
        }

    def push(self, name: str) -> None:
        pass

    @property
    def names(self) -> List[str]:
        return list(self.__events_name.values())

    @property
    def event(self) -> str:
        type = self.__event.type

        if type in self.__events_name:
            return self.__events_name[type]

        return ""

    @property
    def poll(self) -> Generator[str, Any, None]:
        while SDL_PollEvent(byref(self.__event)) != 0:
            yield self.event

    @property
    def wait(self) -> Generator[str, Any, None]:
        while SDL_WaitEvent(byref(self.__event)) != 0:
            yield self.event