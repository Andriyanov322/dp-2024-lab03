from interfaces.imessage import IMessage
import base64


class Base64Decorator(IMessage):
    """
    Декоратор Base64Decorator кодирует содержимое сообщения в Base64.

    Attributes:
        __message (IMessage): Базовое сообщение, которое декорируется.
    """

    def __init__(self, message: IMessage):
        """
        Инициализирует декоратор Base64 с базовым сообщением.

        Args:
            message (IMessage): Объект сообщения для декорирования.
        """
        self.__message = message

    def print(self):
        """Выводит закодированное в Base64 сообщение."""
        encoded_message = self._encode_to_base64(self.__message.get_content())
        print(encoded_message, end="")

    def get_content(self) -> str:
        """
        Возвращает сообщение, закодированное в Base64.

        Returns:
            str: Закодированная строка в формате Base64.
        """
        return self._encode_to_base64(self.__message.get_content())

    def _encode_to_base64(self, content: str) -> str:
        """
        Кодирует переданный текст в Base64.

        Args:
            content (str): Текст для кодирования.

        Returns:
            str: Закодированная строка в формате Base64.
        """
        return base64.b64encode(content.encode()).decode()
