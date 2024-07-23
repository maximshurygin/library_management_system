# Консольное приложение "Система управления библиотекой"

## Описание

Данный проект это консольное приложение для управления библиотекой книг.
Приложение позволяет добавлять, удалять, искать и отображать книги.
Каждая книга содержит следующие поля:

- **id** (уникальный идентификатор, генерируется автоматически)
- **title** (название книги)
- **author** (автор книги)
- **year** (год издания)
- **status** (статус книги: “в наличии”, “выдана”)

## Основные функции

1. **Добавить книгу**:

- Запрашивает у пользователя название книги, автора и год издания.
- Использует метод `add_book` класса `Library` для добавления новой книги в библиотеку.
- Если введен некорректный год, отображается сообщение об ошибке.

2. **Удалить книгу**:

- Запрашивает у пользователя ID книги, которую необходимо удалить.
- Использует метод `delete_book` класса `Library` для удаления книги по ID.

3. **Найти книгу**:

- Запрашивает у пользователя название книги, автора и год издания. Любое из этих полей можно оставить пустым для более гибкого поиска.
- Использует метод `search_book` класса `Library` для поиска книг по указанным критериям.
- Отображает найденные книги или сообщение, если книги не найдены.
- Если введен некорректный год, отображается сообщение об ошибке.

4. **Показать все книги**:

- Использует метод `show_all_books` класса `Library` для отображения списка всех книг в библиотеке.

5. **Изменить статус книги**:

- Запрашивает у пользователя ID книги и новый статус (в наличии или выдана).
- Проверяет корректность введенного статуса.
- Использует метод `change_status` класса `Library` для изменения статуса книги по её ID.
- Обрабатывает ошибки `BookNotFoundError` и `WrongCommandError`.

6. **Выход**:

- Завершает работу программы, выводя сообщение "До свидания!".

## Дополнительная информация

- Хранение данных реализовано в JSON формате.
- Обеспечена корректная обработка ошибок (например, при попытке удалить или изменить несуществующую книгу).
- Для каждой операции написаны функции (добавление, удаление, поиск, отображение, изменение статуса).
- Не были использованы сторонние библиотеки.

## Установка и запуск

1. Клонируйте репозиторий:
   git clone https://github.com/maximshurygin/library_management_system

2. Перейдите в директорию проекта:
   cd library_management_system

3. Запустите приложение:
   python main.py


