from interfaces.imessage import IMessage

class SignatureDecorator(IMessage):
    def __init__(self, message: IMessage, signature: str):
        self._message = message
        self._signature = signature

    def print(self):
        self._message.print()
        print(f"\nС уважением,\n{self._signature}")
