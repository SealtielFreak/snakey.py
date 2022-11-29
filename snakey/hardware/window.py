from ctypes import byref, c_void_p

from sdl2 import *

from snakey.hardware.render_buffer import RenderBuffer
from snakey.hardware.flags import RENDER_GPU, RENDER_CPU, check_valid


class Window:
    def __init__(self, size, title="", flags=RENDER_GPU) -> None:
        check_valid(flags)

        self.__c_window = SDL_CreateWindow(title.encode(),
            SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 
            *size, 
            flags
        )

        self.__render_buffer = RenderBuffer(c_window=self.c_window)
        self.__running = True

    def __del__(self):
        SDL_DestroyWindow(self.__c_window)

    @property
    def c_window(self) -> c_void_p:
        return self.__c_window

    @property
    def render(self) -> RenderBuffer:
        return self.__render_buffer
    
    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running

    def hide(self):
        SDL_HideWindow(self.c_window)

    def show(self):
        SDL_ShowWindow(self.c_window)

    def focus(self):
        SDL_RaiseWindow(self.c_window)
