from interfaces.imessage import IMessage


class HeaderDecorator(IMessage):
    """
    Декоратор HeaderDecorator добавляет заголовок к почтовому сообщению.

    Attributes:
        message (IMessage): Базовое сообщение, которое декорируется.
        header (str): Текст заголовка, добавляемый перед сообщением.
    """

    def __init__(self, message: IMessage, header: str):
        """
        Инициализирует декоратор заголовка с базовым сообщением и заголовком.

        Args:
            __message (IMessage): Объект сообщения для декорирования.
            __header (str): Заголовок, который будет добавлен перед сообщением.
        """
        self.__message = message
        self.__header = header

    def print(self):
        """Выводит заголовок, а затем содержимое сообщения."""
        print(self.__header)
        self.__message.print()
