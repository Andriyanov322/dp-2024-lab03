from datetime import datetime
from interfaces.imessage import IMessage

class DateDecorator(IMessage):
    def __init__(self, message: IMessage):
        self._message = message

    def print(self):
        self._message.print()
        print(f"\nДата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
