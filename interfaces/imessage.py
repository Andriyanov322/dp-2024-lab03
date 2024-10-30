from abc import ABC, abstractmethod

class IMessage(ABC):
    @abstractmethod
    def print(self):
        pass
