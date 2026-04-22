from abc import ABC, abstractmethod


class action(ABC):

    @abstractmethod
    def trigger(self):
        pass
