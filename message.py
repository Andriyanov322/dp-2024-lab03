from interfaces.imessage import IMessage

class Message(IMessage):
    def __init__(self, content: str):
        self.content = content

    def print(self):
        print(self.content)
