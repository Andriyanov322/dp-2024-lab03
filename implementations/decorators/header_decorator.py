from .base_decorator import BaseDecorator

class HeaderDecorator(BaseDecorator):
    """
    Декоратор HeaderDecorator добавляет заголовок к почтовому сообщению.

    Attributes:
        _message (IMessage): Базовое сообщение, которое декорируется.
        _header (str): Текст заголовка, добавляемый перед сообщением.
    """

    def __init__(self, message, header: str):
        """
        Инициализирует декоратор заголовка с базовым сообщением и заголовком.

        Args:
            message (IMessage): Объект сообщения для декорирования.
            header (str): Заголовок, который будет добавлен перед сообщением.
        """
        super().__init__(message)
        self._header = header

    def print(self):
        """Выводит заголовок, а затем содержимое сообщения."""
        print(self._header)
        self._message.print()

    def get_content(self) -> str:
        """
        Возвращает текст с добавленным заголовком.

        Returns:
            str: Текст с заголовком перед сообщением.
        """
        return f"{self._header}\n{self._message.get_content()}"
