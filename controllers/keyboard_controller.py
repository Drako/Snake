from typing import NamedTuple

from pygame.constants import KEYDOWN
from pygame.event import Event

from controllers.controller import Controller
from objects import Snake
from util import Direction


KeyMap = NamedTuple('KeyMap', [('up', int), ('down', int), ('left', int), ('right', int)])


class KeyboardController(Controller):
    _snake: Snake
    _direction: Direction
    _switched_direction: bool
    _key_map: KeyMap

    def __init__(self, *, snake: Snake, start_direction: Direction, key_map: KeyMap):
        self._snake = snake
        self._direction = start_direction
        self._switched_direction = False
        self._key_map = key_map

    def update(self):
        self._snake.move(direction=self._direction)
        self._switched_direction = False

    def handle_event(self, event: Event):
        if event.type == KEYDOWN and not self._switched_direction:
            if event.key == self._key_map.up and self._direction != Direction.DOWN:
                self._direction = Direction.UP
                self._switched_direction = True
            elif event.key == self._key_map.down and self._direction != Direction.UP:
                self._direction = Direction.DOWN
                self._switched_direction = True
            elif event.key == self._key_map.left and self._direction != Direction.RIGHT:
                self._direction = Direction.LEFT
                self._switched_direction = True
            elif event.key == self._key_map.right and self._direction != Direction.LEFT:
                self._direction = Direction.RIGHT
                self._switched_direction = True
