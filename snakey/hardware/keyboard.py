import ctypes
from contextlib import contextmanager
from typing import List

from sdl2 import *


def key_pressed(name: str):
    key_state = SDL_GetKeyboardState(None)
    return key_state[SDL_GetKeyFromName(name.encode())]


def keys_pressed():
    key_state = SDL_GetKeyboardState(None)
    i = 0

    for key in key_state:
        if not key:
            continue

        yield SDL_GetKeyName(i).decode()

        i += 1

        print(i)