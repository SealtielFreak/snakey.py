from sdl2 import *

from snakey.hardware.flags import RENDER_CPU, RENDER_GPU

from snakey.hardware.events import Events
from snakey.hardware.render_buffer import RenderBuffer
from snakey.hardware.window import Window
from snakey.hardware.timing import Timing, sleep_milliseconds, c_sleep_milliseconds


def init(flags):
    SDL_Init(SDL_INIT_EVERYTHING)


def quit():
    SDL_Quit()