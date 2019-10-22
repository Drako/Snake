from pygame.font import Font
from pygame.surface import Surface

from util import Point
from util.colors import WHITE
from . import GameObject


class Score(GameObject):
    _score: int
    _font: Font
    _position: Point

    def __init__(self, *, score: int = 0, font: Font, position: Point):
        self._font = font
        self._position = position
        self._score = score

    def draw_to(self, draw_target: Surface):
        rendered = self._font.render(f'Score: {self._score}', True, WHITE)
        draw_target.blit(rendered, self._position)

    def update(self, *, score: int):
        self._score = score
