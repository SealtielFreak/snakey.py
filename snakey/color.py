import random


class Color:
    def __init__(self, *args) -> None:
        l = len(args)

        self.a = 255
        
        if l == 4:
            self.r, self.g, self.b, self.a = args
        elif l == 3:
            self.r, self.g, self.b = args
        elif l == 0:
            self.r, self.g, self.b = (0, 0, 0)

    def __iter__(self):
        return iter([
            self.r, self.g, self.b, self.a
        ])


def random_color() -> Color:
    rand = lambda: random.randint(0, 255)
    generate = lambda: (rand() for _ in range(3))

    return Color(
        *generate()
    )