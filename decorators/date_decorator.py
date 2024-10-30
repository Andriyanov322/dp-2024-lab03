from interfaces.imessage import IMessage
from datetime import datetime

class DateDecorator(IMessage):
    def __init__(self, message: IMessage):
        self.message = message

    def print(self):
        self.message.print()
        print(datetime.now().strftime("%d.%m.%Y"))
