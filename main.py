from implementations.decorators import HeaderDecorator, SignatureDecorator, DateDecorator, Base64Decorator, BaseDecorator

def main():
    """
    Основная функция программы, демонстрирующая работу декораторов для сообщения.

    Создает базовое сообщение и последовательно декорирует его, добавляя заголовок,
    подпись, дату и кодирование в Base64. Каждый шаг выводится в консоль.
    """
    # Создаем базовое сообщение через BaseDecorator с текстом
    base_message = BaseDecorator(content="С наступающим Новым годом!")
    print("Базовое сообщение:")
    base_message.print()
    print()

    # Добавляем заголовок
    msg_with_header = HeaderDecorator(base_message, "Добрый день,")
    print("Сообщение с заголовком:")
    msg_with_header.print()
    print()

    # Добавляем подпись
    msg_with_signature = SignatureDecorator(msg_with_header, "С уважением, Дед Мороз")
    print("Сообщение с заголовком и подписью:")
    msg_with_signature.print()
    print()

    # Добавляем дату
    msg_with_date = DateDecorator(msg_with_signature)
    print("Сообщение с заголовком, подписью и датой:")
    msg_with_date.print()
    print()

    # Кодируем сообщение в Base64
    final_message = Base64Decorator(msg_with_date)
    print("Закодированное сообщение в Base64:")
    final_message.print()
    print()

if __name__ == "__main__":
    main()
