from interfaces.imessage import IMessage
import base64
import io
import sys


class Base64Decorator(IMessage):
    """
    Декоратор Base64Decorator кодирует содержимое сообщения в Base64.

    Attributes:
        message (IMessage): Базовое сообщение, которое декорируется.
    """

    def __init__(self, message: IMessage):
        """
        Инициализирует декоратор Base64 с базовым сообщением.

        Args:
            message (IMessage): Объект сообщения для декорирования.
        """
        self.message = message

    def print(self):
        """
        Перенаправляет вывод содержимого сообщения в строковый буфер,
        кодирует его в Base64 и выводит закодированную строку в консоль.
        """
        # Перенаправляем вывод в строковый буфер для кодирования
        original_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        self.message.print()
        sys.stdout = original_stdout

        # Кодируем содержимое в Base64
        encoded_message = base64.b64encode(buffer.getvalue().encode()).decode
