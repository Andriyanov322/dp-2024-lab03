import base64
from interfaces.imessage import IMessage

class Base64Decorator(IMessage):
    def __init__(self, message: IMessage):
        self._message = message

    def print(self):
        encoded_text = base64.b64encode(self._message.text.encode()).decode()
        print(f"Сообщение в Base64:\n{encoded_text}")
