import time
from contextlib import contextmanager
from typing import Callable

from sdl2 import *


def sleep_milliseconds(milliseconds: int) -> None:
    time.sleep(milliseconds / 1000.0)


def c_sleep_milliseconds(milliseconds: int) -> None:
    SDL_Delay(milliseconds)


class Timing:
    def __init__(self, frame_rate: int = 60, delay_f: Callable[[int], None] = c_sleep_milliseconds) -> None:
        self.frame_rate = frame_rate
        self.__fps = 0

        self.__current_time = 0
        self.__last_time = 0
        self.__seconds_elapsed = 0
        self.__delay_f = delay_f

    @property
    def delta_time(self) -> float:
        def inner():
            yield (SDL_GetTicks() - self.__last_time) / 1000.0

            self.__last_time = SDL_GetTicks()

        dt = next(inner())
        next(inner())

        return dt

    @property
    def fps(self) -> float:
        return self.__fps

    @property
    def seconds_elapsed(self) -> float:
        return self.__seconds_elapsed

    @property
    @contextmanager
    def current(self):
        seconds_elapsed = lambda end, start: (end - start) / float(SDL_GetPerformanceFrequency())
        performance_frequency = lambda seconds: 1.0 / seconds
        ticks = lambda las_time, frame_rate: int(1000.0 / frame_rate - SDL_GetTicks() + las_time)

        start = SDL_GetPerformanceCounter()
        delay = ticks(self.__last_time, self.frame_rate)

        if delay > 0:
            self.__delay_f(delay)

        yield self.delta_time

        end = SDL_GetPerformanceCounter()

        self.__seconds_elapsed = seconds_elapsed(end, start)
        self.__fps = performance_frequency(self.__seconds_elapsed)
        self.__last_time = SDL_GetTicks()

    def __str__(self) -> str:
        return f"FPS: {self.fps}, Delta time: {self.delta_time}, Seconds elapsed: {self.seconds_elapsed}"
