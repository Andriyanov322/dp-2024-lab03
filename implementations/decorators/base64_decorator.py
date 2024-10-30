from interfaces.imessage import IMessage
import base64
import io
from contextlib import redirect_stdout


class Base64Decorator(IMessage):
    """
    Декоратор Base64Decorator кодирует содержимое сообщения в Base64.
    """

    def __init__(self, message: IMessage):
        """
        Инициализирует декоратор Base64 с базовым сообщением.

        Args:
            message (IMessage): Объект сообщения для декорирования.
        """
        self.__message = message

    def print(self):
        """
        Захватывает вывод содержимого сообщения, кодирует его в Base64 и выводит.
        """
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.__message.print()

        encoded_message = self._encode_to_base64(buffer.getvalue())
        print(encoded_message, end="")

    def _encode_to_base64(self, content: str) -> str:
        """
        Кодирует переданный текст в Base64.

        Args:
            content (str): Текст для кодирования.

        Returns:
            str: Закодированная строка в формате Base64.
        """
        return base64.b64encode(content.encode()).decode()

