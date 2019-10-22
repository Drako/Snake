import pygame
from pygame.surface import Surface

from util import Rect
from util.colors import WHITE
from . import GameObject


class Field(GameObject):
    _area: Rect

    def __init__(self, *, area: Rect):
        self._area = area

    def draw_to(self, draw_target: Surface):
        pygame.draw.rect(draw_target, WHITE, self._area, 1)

    def client_area(self) -> Rect:
        return Rect(self._area.x + 1, self._area.y + 1, self._area.w - 2, self._area.h - 2)
