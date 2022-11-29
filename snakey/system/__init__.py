import ctypes

from sdl2 import *


class System:
    @staticmethod
    def init():
        if SDL_Init(SDL_INIT_EVERYTHING) != 0:
            SDL_Log(b"Unable to initialize SDL: %s", SDL_GetError())

    @staticmethod
    def over():
        SDL_QUIT()


class Event:
    def __init__(self):
        self.__event = SDL_Event()

    @property
    def type(self):
        return self.__event.type


class Window:
    def __init__(self, title: str, size=(640, 480)):
        self.__window = SDL_CreateWindow(title.encode(), SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, *size, SDL_WINDOW_SHOWN)

        if self.__window is None:
            raise RuntimeError("Window is not created")

    def destroy(self):
        SDL_DestroyWindow(self.__window)

    def poll_event(self, event: Event):
        SDL_PollEvent(ctypes.byref(event.__event))


class Screen: ...