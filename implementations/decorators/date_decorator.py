from interfaces.imessage import IMessage
from datetime import datetime


class DateDecorator(IMessage):
    """
    Декоратор DateDecorator добавляет текущую дату к почтовому сообщению.

    Attributes:
        message (IMessage): Базовое сообщение, которое декорируется.
    """

    def __init__(self, message: IMessage):
        """
        Инициализирует декоратор даты с базовым сообщением.

        Args:
            message (IMessage): Объект сообщения для декорирования.
        """
        self.__message = message

    def print(self):
        """Выводит содержимое сообщения, а затем текущую дату в формате ДД.ММ.ГГГГ."""
        self.__message.print()
        print(datetime.now().strftime("%d.%m.%Y"))

    def get_content(self) -> str:
        """
        Возвращает текст с добавленной датой.

        Returns:
            str: Текст сообщения с текущей датой.
        """
        return f"{self.__message.get_content()}\n{datetime.now().strftime('%d.%m.%Y')}"
