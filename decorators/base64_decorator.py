from interfaces.imessage import IMessage
import base64
import io
import sys

class Base64Decorator(IMessage):
    def __init__(self, message: IMessage):
        self.message = message

    def print(self):
        # Перенаправляем вывод в строку, чтобы закодировать
        original_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        self.message.print()
        sys.stdout = original_stdout
        # Кодируем содержимое
        encoded_message = base64.b64encode(buffer.getvalue().encode()).decode()
        print(encoded_message)
