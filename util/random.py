from random import randint

from . import Rect, Point, Direction


def random_rect(*, size: int, area: Rect) -> Rect:
    return Rect(
        x=randint(area.x, area.x + area.w - 1 - size),
        y=randint(area.y, area.y + area.h - 1 - size),
        w=size,
        h=size,
    )


def random_point(*, offset: int, area: Rect) -> Point:
    return Point(
        x=randint(area.x + offset, area.x + area.w - 1 - offset),
        y=randint(area.y + offset, area.y + area.h - 1 - offset),
    )


def random_direction() -> Direction:
    return Direction(randint(0, 3))
