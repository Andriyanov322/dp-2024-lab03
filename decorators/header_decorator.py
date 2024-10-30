from interfaces.imessage import IMessage

class HeaderDecorator(IMessage):
    def __init__(self, message: IMessage, header: str):
        self._message = message
        self._header = header

    def print(self):
        print(f"{self._header}\n" + "-" * len(self._header))
        self._message.print()
