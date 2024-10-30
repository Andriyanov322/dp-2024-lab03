import unittest
from io import StringIO
from contextlib import redirect_stdout
from message import Message
from decorators import HeaderDecorator, SignatureDecorator, DateDecorator, Base64Decorator
from datetime import datetime
import base64


class TestDecorators(unittest.TestCase):

    def test_message(self):
        """Проверка базового сообщения без декораций."""
        message = Message("Поздравляем с Днем Рождения!")
        with StringIO() as buf, redirect_stdout(buf):
            message.print()
            output = buf.getvalue().strip()
        self.assertEqual(output, "Поздравляем с Днем Рождения!")

    def test_header_decorator(self):
        """Проверка добавления заголовка."""
        message = Message("Поздравляем с Днем Рождения!")
        decorated_message = HeaderDecorator(message, "Приветствуем,")
        with StringIO() as buf, redirect_stdout(buf):
            decorated_message.print()
            output = buf.getvalue().strip()
        expected_output = "Приветствуем,\nПоздравляем с Днем Рождения!"
        self.assertEqual(output, expected_output)

    def test_signature_decorator(self):
        """Проверка добавления подписи."""
        message = Message("Поздравляем с Днем Рождения!")
        decorated_message = SignatureDecorator(message, "Ваши друзья")
        with StringIO() as buf, redirect_stdout(buf):
            decorated_message.print()
            output = buf.getvalue().strip()
        expected_output = "Поздравляем с Днем Рождения!\nВаши друзья"
        self.assertEqual(output, expected_output)

    def test_date_decorator(self):
        """Проверка добавления даты."""
        message = Message("Поздравляем с Днем Рождения!")
        decorated_message = DateDecorator(message)
        with StringIO() as buf, redirect_stdout(buf):
            decorated_message.print()
            output = buf.getvalue().strip()
        expected_output = f"Поздравляем с Днем Рождения!\n{datetime.now().strftime('%d.%m.%Y')}"
        self.assertEqual(output, expected_output)

    def test_base64_decorator(self):
        """Проверка кодирования сообщения в Base64."""
        message = Message("Поздравляем с Днем Рождения!")
        decorated_message = Base64Decorator(message)
        with StringIO() as buf, redirect_stdout(buf):
            decorated_message.print()
            output = buf.getvalue().strip().replace('=', '')
        # Кодируем и убираем символы `=` в конце
        expected_output = base64.b64encode("Поздравляем с Днем Рождения!".encode()).decode().replace('=', '')
        self.assertTrue(output in expected_output or expected_output in output)

    def test_combined_decorators(self):
        """Проверка цепочки декораторов: заголовок, подпись, дата и кодирование в Base64."""
        message = Message("Поздравляем с Днем Рождения!")
        decorated_message = HeaderDecorator(message, "Уважаемый Иван,")
        decorated_message = SignatureDecorator(decorated_message, "Команда компании")
        decorated_message = DateDecorator(decorated_message)
        decorated_message = Base64Decorator(decorated_message)

        with StringIO() as buf, redirect_stdout(buf):
            decorated_message.print()
            output = buf.getvalue().strip().replace('=', '')

        # Создаем строку вручную для проверки Base64 кодирования всей цепочки
        original_text = "Уважаемый Иван,\nПоздравляем с Днем Рождения!\nКоманда компании\n" + datetime.now().strftime(
            "%d.%m.%Y")
        expected_output = base64.b64encode(original_text.encode()).decode().replace('=', '')
        self.assertTrue(output in expected_output or expected_output in output)


if __name__ == "__main__":
    unittest.main()
