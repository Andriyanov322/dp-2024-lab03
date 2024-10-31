from .base_decorator import BaseDecorator

class SignatureDecorator(BaseDecorator):
    """
    Декоратор SignatureDecorator добавляет подпись к почтовому сообщению.

    Attributes:
        _message (IMessage): Базовое сообщение, которое декорируется.
        _signature (str): Текст подписи, добавляемый в конце сообщения.
    """

    def __init__(self, message, signature: str):
        """
        Инициализирует декоратор подписи с базовым сообщением и подписью.

        Args:
            message (IMessage): Объект сообщения для декорирования.
            signature (str): Подпись, которая будет добавлена в конце сообщения.
        """
        super().__init__(message)
        self._signature = signature

    def print(self):
        """Выводит содержимое сообщения, а затем подпись."""
        self._message.print()
        print(self._signature)

    def get_content(self) -> str:
        """
        Возвращает текст с добавленной подписью.

        Returns:
            str: Текст сообщения с подписью.
        """
        return f"{self._message.get_content()}\n{self._signature}"
