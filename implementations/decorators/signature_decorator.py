from interfaces.imessage import IMessage


class SignatureDecorator(IMessage):
    """
    Декоратор SignatureDecorator добавляет подпись к почтовому сообщению.

    Attributes:
        message (IMessage): Базовое сообщение, которое декорируется.
        signature (str): Текст подписи, добавляемый в конце сообщения.
    """

    def __init__(self, message: IMessage, signature: str):
        """
        Инициализирует декоратор подписи с базовым сообщением и подписью.

        Args:
            message (IMessage): Объект сообщения для декорирования.
            signature (str): Подпись, которая будет добавлена в конце сообщения.
        """
        self.message = message
        self.signature = signature

    def print(self):
        """Выводит содержимое сообщения, а затем подпись."""
        self.message.print()
        print(self.signature)
