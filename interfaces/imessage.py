from abc import ABC, abstractmethod


class IMessage(ABC):
    """
    Интерфейс IMessage представляет структуру базового почтового сообщения.
    Все классы сообщений, реализующие этот интерфейс, должны содержать методы `print` и `get_content`,
    которые выводят и возвращают содержимое сообщения соответственно.
    """

    @abstractmethod
    def print(self):
        """Выводит сообщение в консоль."""
        pass

    @abstractmethod
    def get_content(self) -> str:
        """Возвращает содержимое сообщения."""
        pass
