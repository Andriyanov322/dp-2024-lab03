import unittest
from io import StringIO
from contextlib import redirect_stdout
from implementations.decorators import HeaderDecorator, SignatureDecorator, DateDecorator, Base64Decorator, BaseDecorator
from datetime import datetime
import base64

class TestDecorators(unittest.TestCase):

    def setUp(self):
        """Создаем базовое сообщение с использованием BaseDecorator."""
        self.base_message = BaseDecorator(content="Тестовое сообщение")

    def test_base64_decorator(self):
        """Проверка кодирования сообщения в Base64."""
        decorated_message = Base64Decorator(self.base_message)

        # Тестируем print()
        with StringIO() as buf, redirect_stdout(buf):
            decorated_message.print()
            output = buf.getvalue().strip()
        expected_output = base64.b64encode("Тестовое сообщение".encode()).decode()
        self.assertEqual(output, expected_output)

        # Тестируем get_content()
        self.assertEqual(decorated_message.get_content(), expected_output)

    def test_date_decorator(self):
        """Проверка добавления даты."""
        decorated_message = DateDecorator(self.base_message)

        # Тестируем print()
        with StringIO() as buf, redirect_stdout(buf):
            decorated_message.print()
            output = buf.getvalue().strip()
        expected_output = f"Тестовое сообщение\n{datetime.now().strftime('%d.%m.%Y')}"
        self.assertEqual(output, expected_output)

        # Тестируем get_content()
        self.assertEqual(decorated_message.get_content(), expected_output)

    def test_header_decorator(self):
        """Проверка добавления заголовка."""
        decorated_message = HeaderDecorator(self.base_message, "Заголовок:")

        # Тестируем print()
        with StringIO() as buf, redirect_stdout(buf):
            decorated_message.print()
            output = buf.getvalue().strip()
        expected_output = "Заголовок:\nТестовое сообщение"
        self.assertEqual(output, expected_output)

        # Тестируем get_content()
        self.assertEqual(decorated_message.get_content(), expected_output)

    def test_signature_decorator(self):
        """Проверка добавления подписи."""
        decorated_message = SignatureDecorator(self.base_message, "Подпись")

        # Тестируем print()
        with StringIO() as buf, redirect_stdout(buf):
            decorated_message.print()
            output = buf.getvalue().strip()
        expected_output = "Тестовое сообщение\nПодпись"
        self.assertEqual(output, expected_output)

        # Тестируем get_content()
        self.assertEqual(decorated_message.get_content(), expected_output)

    def test_combined_decorators(self):
        """Проверка цепочки декораторов: заголовок, подпись, дата и кодирование в Base64."""
        decorated_message = HeaderDecorator(self.base_message, "Заголовок:")
        decorated_message = SignatureDecorator(decorated_message, "Подпись")
        decorated_message = DateDecorator(decorated_message)
        decorated_message = Base64Decorator(decorated_message)

        # Создаем строку для проверки Base64 кодирования всей цепочки
        original_text = f"Заголовок:\nТестовое сообщение\nПодпись\n{datetime.now().strftime('%d.%m.%Y')}"
        expected_output = base64.b64encode(original_text.encode()).decode()

        # Тестируем print()
        with StringIO() as buf, redirect_stdout(buf):
            decorated_message.print()
            output = buf.getvalue().strip()
        self.assertEqual(output, expected_output)

        # Тестируем get_content()
        self.assertEqual(decorated_message.get_content(), expected_output)


if __name__ == "__main__":
    unittest.main()
