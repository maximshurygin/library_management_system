from library.exceptions import BookNotFoundError, WrongCommandError
from library.library import Library


def main():
    """
    Основная функция для управления библиотечной системой через командную строку.
    """
    book_library = Library()

    while True:
        # Показать меню команд
        print("\n1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        # Запрос команды у пользователя
        user_command = input("Введите номер нужной команды: ")

        if user_command == "1":
            # Добавление книги
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                year = int(input("Введите год издания книги: "))
                book_library.add_book(title, author, year)
            except ValueError:
                print("Неверный формат года издания. Попробуйте снова")

        elif user_command == "2":
            # Удаление книги
            book_id = input("Введите ID книги для удаления: ")
            book_library.delete_book(book_id)

        elif user_command == "3":
            # Поиск книги
            title = input("Введите название книги (или оставьте пустым): ")
            author = input("Введите автора книги (или оставьте пустым): ")
            year = input("Введите год издания книги (или оставьте пустым): ")
            try:
                year = int(year) if year else None
                found_books = book_library.search_book(title, author, year)
                if found_books:
                    for book in found_books:
                        print(book)
                else:
                    print("По вашему запросу нет результата.")
            except ValueError:
                print("Год издания должен быть числом. Попробуйте снова.")

        elif user_command == "4":
            # Показать все книги
            book_library.show_all_books()

        elif user_command == "5":
            # Изменение статуса книги
            try:
                book_id = input("Введите ID книги: ")

                status_number = input("Выберите новый статуст книги:\n1 - в наличии\n2 - выдана\n")
                if status_number not in ["1", "2"]:
                    raise WrongCommandError("Нужно отправить цифру 1 или 2. Поробуйте снова")

                new_status = "в наличии" if status_number == "1" else "выдана"
                book_library.change_status(book_id, new_status)

            except BookNotFoundError as e:
                print(e)
            except WrongCommandError as e:
                print(e)
        elif user_command == "6":
            # Завершение работы программы
            print("Досвидания!")
            break
        else:
            # Обработка неверной команды
            print("Такой команды нет")


if __name__ == "__main__":
    main()
