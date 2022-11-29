import math

from snakey import Vector2
from snakey.color import Color
from snakey.drawables import primitives
from snakey.hardware import Window, Timing, Events
from snakey.hardware.keyboard import key_pressed, keys_pressed
from snakey.nodes import RectangleShape
from snakey.nodes.transformable import translate, rotate, mid_vertices


to_radians = lambda n: (math.pi / 180) * n

if __name__ == '__main__':
    window = Window(size=(640, 480))
    timing = Timing(60)
    shape = RectangleShape(100, 100) | translate(Vector2(150, 320))

    shape.origin = mid_vertices(shape.transform.vertices)

    while window.running:
        events = Events()

        for event in events.poll:
            window.running = not event == "closed"

        print(key_pressed("W"))

        window.render.clear(Color(255, 255, 255))

        with timing.current:
            primitives.filled_polygon(window.render, (shape | rotate(to_radians(60 * timing.delta_time))).transform.vertices, Color(255, 0, 0))

        window.render.present()

"""

"""
