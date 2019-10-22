import pygame
from pygame.surface import Surface

from util import Rect, Point
from util.collisions import rect_contains_point
from util.colors import WHITE
from . import GameObject


class Goal(GameObject):
    _area: Rect

    def __init__(self, *, area: Rect):
        self._area = area

    def draw_to(self, draw_target: Surface):
        pygame.draw.rect(draw_target, WHITE, self._area)

    def __contains__(self, point: Point):
        return rect_contains_point(self._area, point)

    def move_to(self, area: Rect):
        self._area = area
