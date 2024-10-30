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
            message (IMessage): Объект сообщения для декорирования.
            header (str): Заголовок, который будет добавлен перед сообщением.
        """
        self.__message = message
        self.__header = header

    def print(self):
        """Выводит заголовок, а затем содержимое сообщения."""
        print(self.__header)
        self.__message.print()

    def get_content(self) -> str:
        """
        Возвращает текст с добавленным заголовком.

        Returns:
            str: Текст с заголовком перед сообщением.
        """
        return f"{self.__header}\n{self.__message.get_content()}"
