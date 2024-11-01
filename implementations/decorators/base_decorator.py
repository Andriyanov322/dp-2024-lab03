from interfaces.imessage import IMessage

class BaseDecorator(IMessage):
    """
    Базовый декоратор, от которого наследуются все остальные декораторы.

    Attributes:
        _message (IMessage): Базовое сообщение, которое декорируется.
        _content (str): Содержимое сообщения, если нет декорируемого объекта.
    """

    def __init__(self, message=None, content=""):
        """
        Инициализирует базовый декоратор с сообщением или текстом.

        Args:
            message (IMessage, optional): Объект сообщения для декорирования.
            content (str, optional): Содержимое сообщения, если message отсутствует.
        """
        self._message = message
        self._content = content

    def print(self):
        """Выводит только content, если нет декорируемого объекта."""
        print(self._content)

    def get_content(self) -> str:
        """Возвращает содержимое базового сообщения или контент, если нет декорируемого объекта."""
        return self._message.get_content() if self._message else self._content
