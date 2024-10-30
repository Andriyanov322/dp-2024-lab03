from message import EmailMessage
from decorators.header_decorator import HeaderDecorator
from decorators.signature_decorator import SignatureDecorator
from decorators.date_decorator import DateDecorator
from decorators.base64_decorator import Base64Decorator

if __name__ == "__main__":
    # Исходное сообщение
    email = EmailMessage("Привет! Это тестовое сообщение.")

    # Добавляем декораторы
    email = HeaderDecorator(email, "Заголовок: Важное сообщение")
    email = SignatureDecorator(email, "Иван Иванов")
    email = DateDecorator(email)
    email = Base64Decorator(email)

    # Выводим сообщение
    email.print()
