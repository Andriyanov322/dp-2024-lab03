from .base_decorator import BaseDecorator
import base64

class Base64Decorator(BaseDecorator):
    """
    Декоратор Base64Decorator кодирует содержимое сообщения в Base64.

    Attributes:
        _message (IMessage): Базовое сообщение, которое декорируется.
    """

    def print(self):
        """Выводит закодированное в Base64 сообщение."""
        print(self.get_content(), end="")

    def get_content(self) -> str:
        """
        Возвращает сообщение, закодированное в Base64.

        Returns:
            str: Закодированная строка в формате Base64.
        """
        return self._encode_to_base64(self._message.get_content())

    def _encode_to_base64(self, content: str) -> str:
        """
        Кодирует переданный текст в Base64.

        Args:
            content (str): Текст для кодирования.

        Returns:
            str: Закодированная строка в формате Base64.
        """
        return base64.b64encode(content.encode()).decode()
