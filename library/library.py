import json
import os

from library.book import Book
from library.exceptions import BookNotFoundError


class Library:
    """
    Класс, представляющий библиотечную систему.

    Атрибуты:
        file_path (str): Путь к файлу для хранения данных о книгах.
        books (list): Список книг в библиотеке.
    """

    def __init__(self, file_path: str = "data/books.json"):
        """
        Инициализирует экземпляр класса Library.

        Args:
            file_path (str, optional): Путь к файлу для хранения данных о книгах. По умолчанию "data/books.json".
        """

        self.file_path = file_path
        self.books = self.load_books()

    def load_books(self):
        """
        Загружает книги из файла.

        Returns:
            list: Список объектов Book.
        """

        if os.path.exists("data/books.json"):
            with open("data/books.json", "r", encoding="utf-8") as file:
                books = json.load(file)
                return [Book.from_dict(book) for book in books]
        return []

    def save_books(self):
        """
        Сохраняет книги в файл.
        """

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """
        Добавляет новую книгу в библиотеку.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
        """

        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.save_books()
        print("Книга успешно добавлена!\n")

    def delete_book(self, book_id: str):
        """
        Удаляет книгу из библиотеки по её ID.

        Args:
            book_id (str): Уникальный идентификатор книги.
        """

        try:
            if not any(book.id == book_id for book in self.books):
                raise BookNotFoundError(f"Книга с ID {book_id} не найдена\n")
            self.books = [book for book in self.books if book.id != book_id]
            self.save_books()
            print("Книга успешно удалена!\n")
        except BookNotFoundError as e:
            print(e)

    def search_book(self, title: str = None, author: str = None, year: int = None):
        """
        Ищет книги в библиотеке по названию, автору или году издания.

        Args:
            title (str, optional): Название книги.
            author (str, optional): Автор книги.
            year (int, optional): Год издания книги.

        Returns:
            list: Список книг, соответствующих критериям поиска.
        """

        results = self.books
        if title:
            results = [book for book in results if book.title == title]
        if author:
            results = [book for book in results if book.author == author]
        if year:
            results = [book for book in results if book.year == year]
        return results

    def show_all_books(self):
        """
        Отображает все книги в библиотеке.
        """

        if not self.books:
            print("Книг нет в данный момент\n")
        for book in self.books:
            print(book)

    def change_status(self, book_id: str, new_status: str):
        """
        Изменяет статус книги по её ID.

        Args:
            book_id (str): Уникальный идентификатор книги.
            new_status (str): Новый статус книги ("в наличии" или "выдана").
        """

        if new_status not in ["в наличии", "выдана"]:
            raise ValueError("Некорректный статус. Допустимые статусы: 'в наличии' или 'выдана'.")

        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                print("Статус успешно изменен!\n")
                return

        raise BookNotFoundError(f"Книга с ID {book_id} не найдена.")

    def check_book_id(self, book_id):
        """
        Проверяет существование книги по её ID.

        Args:
            book_id (str): Уникальный идентификатор книги.

        Returns:
            bool: True, если книга с таким ID существует, иначе False.
        """

        return any(book.id == book_id for book in self.books)
