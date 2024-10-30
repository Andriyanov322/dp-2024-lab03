from interfaces.imessage import IMessage

class EmailMessage(IMessage):
    def __init__(self, text: str):
        self._text = text

    def print(self):
        print(self._text)

    @property
    def text(self) -> str:
        return self._text
