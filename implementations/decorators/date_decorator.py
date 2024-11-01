from .base_decorator import BaseDecorator
from datetime import datetime

class DateDecorator(BaseDecorator):
    """
    Декоратор DateDecorator добавляет текущую дату к почтовому сообщению.

    Attributes:
        _message (IMessage): Базовое сообщение, которое декорируется.
    """

    def print(self):
        """Выводит содержимое сообщения, а затем текущую дату в формате ДД.ММ.ГГГГ."""
        self._message.print()
        print(datetime.now().strftime("%d.%m.%Y"))

    def get_content(self) -> str:
        """
        Возвращает текст с добавленной датой.

        Returns:
            str: Текст сообщения с текущей датой.
        """
        return f"{self._message.get_content()}\n{datetime.now().strftime('%d.%m.%Y')}"
