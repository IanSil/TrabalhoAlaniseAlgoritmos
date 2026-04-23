from abc import ABC, abstractmethod


class Action(ABC):

    @abstractmethod
    def trigger(self):
        pass
