from collections import deque
from typing import Deque

from pygame.pixelarray import PixelArray
from pygame.surface import Surface

from util import Direction, Point
from util.colors import WHITE
from . import GameObject


class Snake(GameObject):
    _points: Deque[Point]

    def __init__(self, *, starting_point: Point):
        self._points = deque(maxlen=100)
        self._points.append(starting_point)

    def draw_to(self, draw_target: Surface):
        with PixelArray(draw_target) as pixels:
            for x, y in self._points:
                pixels[x][y] = WHITE

    def head(self) -> Point:
        return self._points[-1]

    def grow(self):
        self._points = deque(self._points, maxlen=self._points.maxlen + 25)

    def move(self, *, direction: Direction):
        head = self.head()
        if direction == Direction.UP:
            head = Point(x=head.x, y=head.y - 1)
        elif direction == Direction.DOWN:
            head = Point(x=head.x, y=head.y + 1)
        elif direction == Direction.LEFT:
            head = Point(x=head.x - 1, y=head.y)
        else:
            head = Point(x=head.x + 1, y=head.y)
        self._points.append(head)

    def __len__(self):
        return len(self._points)

    def __iter__(self):
        return iter(self._points)
