from abc import abstractmethod, ABC

from pygame.event import Event


class Controller(ABC):
    def handle_event(self, event: Event):
        pass

    @abstractmethod
    def update(self):
        pass
