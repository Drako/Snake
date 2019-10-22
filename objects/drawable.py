from abc import ABC, abstractmethod

from pygame.surface import Surface


class Drawable(ABC):
    @abstractmethod
    def draw_to(self, draw_target: Surface):
        pass
