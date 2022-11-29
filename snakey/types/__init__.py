import ctypes


def c_array(t):
    def inner(size: int, points: list):
        return (t * size)(*points)

    return inner


c_int16_array = c_array(ctypes.c_int16)
