from sdl2.sdlgfx import *
from snakey.types import *

from snakey import Color
from snakey.hardware import RenderBuffer


def filled_polygon(buffer: RenderBuffer, vertices: list, color: Color):
    to_c = lambda points: c_int16_array(len(points), points)
    vertices_x, vertices_y = [], []

    for vec in vertices:
        vertices_x.append(int(vec[0]))
        vertices_y.append(int(vec[1]))

    filledPolygonRGBA(buffer.c_buffer, to_c(vertices_x), to_c(vertices_y), len(vertices), *color)
