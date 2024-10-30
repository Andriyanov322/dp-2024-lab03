from interfaces.imessage import IMessage


class Message(IMessage):
    """
    Класс Message представляет базовое почтовое сообщение.

    Attributes:
        __content (str): Текст сообщения.
    """

    def __init__(self, content: str):
        """
        Инициализирует экземпляр Message с указанным содержимым.

        Args:
            __content (str): Текст сообщения.
        """
        self.__content = content

    def print(self):
        """Выводит текст сообщения в консоль."""
        print(self.__content)
