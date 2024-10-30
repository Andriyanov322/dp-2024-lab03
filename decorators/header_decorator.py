from interfaces.imessage import IMessage

class HeaderDecorator(IMessage):
    def __init__(self, message: IMessage, header: str):
        self.message = message
        self.header = header

    def print(self):
        print(self.header)
        self.message.print()
