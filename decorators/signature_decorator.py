from interfaces.imessage import IMessage

class SignatureDecorator(IMessage):
    def __init__(self, message: IMessage, signature: str):
        self.message = message
        self.signature = signature

    def print(self):
        self.message.print()
        print(self.signature)
