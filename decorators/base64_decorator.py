from interfaces.imessage import IMessage
import base64
import io
from contextlib import redirect_stdout


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
        Захватывает вывод содержимого сообщения в строковый буфер,
        кодирует его в Base64 и выводит закодированную строку.
        """
        buffer = io.StringIO()
        # Перенаправляем вывод в буфер и вызываем print у декорированного сообщения
        with redirect_stdout(buffer):
            self.message.print()

        # Кодируем содержимое буфера в Base64
        encoded_message = base64.b64encode(buffer.getvalue().encode()).decode()
        print(encoded_message, end="")  # Убираем автоматическое добавление новой строки
