from . import Point, Rect


def rect_contains_point(rect: Rect, point: Point):
    return (rect.x <= point.x < (rect.x + rect.w)
            and rect.y <= point.y < (rect.y + rect.h))
