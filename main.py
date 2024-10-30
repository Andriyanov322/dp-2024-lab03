from implementations.message import Message
from implementations.decorators.header_decorator import HeaderDecorator
from implementations.decorators.signature_decorator import SignatureDecorator
from implementations.decorators.date_decorator import DateDecorator
from implementations.decorators.base64_decorator import Base64Decorator


def main():
    """
    Основная функция программы, демонстрирующая работу декораторов для сообщения.

    Создает базовое сообщение и последовательно декорирует его, добавляя заголовок,
    подпись, дату и кодирование в Base64. Каждый шаг выводится в консоль.
    """
    # Базовое сообщение
    message = Message("С наступающим Новым годом!")
    message.print()

    # Добавляем заголовок
    msg_with_header = HeaderDecorator(message, "Добрый день,")
    msg_with_header.print()

    # Добавляем подпись
    msg_with_header_and_footer = SignatureDecorator(msg_with_header, "Дед Мороз")
    msg_with_header_and_footer.print()

    # Добавляем дату
    msg_with_header_footer_and_date = DateDecorator(msg_with_header_and_footer)
    msg_with_header_footer_and_date.print()

    # Кодируем сообщение в Base64
    msg_with_header_footer_date_in_base64 = Base64Decorator(msg_with_header_footer_and_date)
    msg_with_header_footer_date_in_base64.print()


if __name__ == "__main__":
    main()
