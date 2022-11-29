from ctypes import byref, c_void_p

from sdl2 import *

from snakey.color import Color
from snakey.hardware.flags import RENDER_GPU, RENDER_CPU, check_valid


class RenderBuffer:
    def __init__(self, c_window=None, index=-1, flags=RENDER_GPU) -> None:
        check_valid(flags)
        self.__c_renderer = SDL_CreateRenderer(c_window, index, flags)
        self.__color = Color()

    def __del__(self):
        SDL_DestroyRenderer(self.__c_renderer)

    @property
    def c_buffer(self) -> c_void_p:
        return self.__c_renderer
        
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: Color):
        self.__color = color
        SDL_SetRenderDrawColor(self.c_buffer, *color)

    def clear(self, color: Color = Color()):
        SDL_SetRenderDrawColor(self.c_buffer, *color)
        SDL_RenderClear(self.c_buffer)

    def present(self):
        SDL_RenderPresent(self.c_buffer)
