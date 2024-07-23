import json
import os
import unittest

from library.book import Book
from library.library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        """
        Метод для подготовки окружения перед каждым тестом.
        """
        self.test_file_path = "test_books.json"
        self.library = Library(self.test_file_path)

    def tearDown(self):
        """
        Метод для очистки окружения после каждого теста.
        """
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_library_initialization(self):
        """
        Тест для проверки инициализации библиотеки.
        """
        self.assertEqual(self.library.file_path, self.test_file_path)
        self.assertEqual(self.library.books, [])

    def test_load_books(self):
        """
        Тест для проверки загрузки книг.
        """
        self.assertEqual(self.library.load_books(), [])

    def test_save_books(self):
        """
        Тест для проверки сохранения книг в файл.
        """
        book = Book("Test", "John", 2007)
        self.library.books.append(book)
        self.library.save_books()
        with open(self.test_file_path, "r", encoding="utf-8") as file:
            books = json.load(file)
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["title"], "Test")

    def test_add_book(self):
        """
        Тест для проверки добавления новой книги в библиотеку.
        """
        self.library.add_book("Some Title", "John", 2008)
        with open(self.test_file_path, "r", encoding="utf-8") as file:
            books = json.load(file)
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["title"], "Some Title")
        self.assertEqual(books[0]["author"], "John")
        self.assertEqual(books[0]["year"], 2008)

    def test_delete_book(self):
        """
        Тест для проверки удаления книги из библиотеки по ID.
        """
        book = Book("Test", "Nick", 2009)
        self.library.books.append(book)
        self.library.save_books()
        self.library.delete_book(book.id)
        self.assertEqual(len(self.library.books), 0)

    def test_search_book(self):
        """
        Тест для проверки поиска книг по названию, автору и году (в любых комбинациях).
        """
        book = Book("New Test", "Dan", 2010)
        self.library.books.append(book)
        self.library.save_books()
        search_result_1 = self.library.search_book(title="New Test")
        search_result_2 = self.library.search_book(author="Dan")
        search_result_3 = self.library.search_book(year=2010)
        search_result_4 = self.library.search_book(title="New Test", author="Dan")
        search_result_5 = self.library.search_book(title="New Test", author="Dan", year=2010)
        search_result_6 = self.library.search_book(title="New Test", year=2010)
        search_result_7 = self.library.search_book(author="Dan", year=2010)

        self.assertEqual(book, *search_result_1)
        self.assertEqual(book, *search_result_2)
        self.assertEqual(book, *search_result_3)
        self.assertEqual(book, *search_result_4)
        self.assertEqual(book, *search_result_5)
        self.assertEqual(book, *search_result_6)
        self.assertEqual(book, *search_result_7)

    def test_change_status(self):
        """
        Тест для проверки изменения статуса книги по ID.
        """
        book = Book("Test!", "Author!", 2000)
        self.library.books.append(book)
        self.library.save_books()
        self.library.change_status(book.id, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

    def test_check_book_id(self):
        """
        Тест метода проверки существования книги по её ID.
        """
        book = Book("Test Book", "Test Author", 2024)
        self.library.books.append(book)
        self.assertTrue(self.library.check_book_id(book.id))
        self.assertFalse(self.library.check_book_id("123456"))


if __name__ == "__main__":
    unittest.main()
