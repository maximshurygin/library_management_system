import unittest
import uuid

from library.book import Book


class TestBook(unittest.TestCase):

    def test_book_initialization_with_id(self):
        """
        Тест инициализации книги с указанным ID.
        """
        book_id = str(uuid.uuid4())
        book = Book("Test1", "John", 2000, book_id)

        # Проверяем, что все атрибуты соответствуют ожиданиям
        self.assertEqual(book.id, book_id)
        self.assertEqual(book.title, "Test1")
        self.assertEqual(book.author, "John")
        self.assertEqual(book.year, 2000)
        self.assertEqual(book.status, "в наличии")

    def test_book_initialization_without_id(self):
        """
        Тест инициализации книги без указанния ID.
        """
        book = Book("Test2", "Nick", 2001)

        # Проверяем, что все атрибуты соответствуют ожиданиям
        self.assertIsNotNone(book.id)
        self.assertEqual(book.title, "Test2")
        self.assertEqual(book.author, "Nick")
        self.assertEqual(book.year, 2001)
        self.assertEqual(book.status, "в наличии")

    def test_repr(self):
        """
        Тест строкового представления книги.
        """
        book = Book("Test3", "Dan", 2002)
        expected_repr = f"ID: {book.id}, название: {book.title}, автор: {book.author}, год издания: {book.year}, статус: {book.status}"
        self.assertEqual(repr(book), expected_repr)

    def test_to_dict(self):
        """
        Тест метода для преобразования объекта Book в словарь.
        """
        book = Book("Test4", "Alex", 2003)
        expected_dict = {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "status": book.status
        }
        self.assertEqual(book.to_dict(), expected_dict)

    def test_from_dict(self):
        """
        Тест метода для создания объекта книги из словаря.
        """
        book_id = str(uuid.uuid4())
        test_dict = {
            "id": book_id,
            "title": "Test5",
            "author": "Mike",
            "year": 2004,
            "status": "в наличии"
        }
        expected_book = Book("Test5", "Mike", 2004, book_id)
        book_from_dict = Book.from_dict(test_dict)

        # Проверяем, что все атрибуты соответствуют ожиданиям
        self.assertEqual(book_from_dict.id, expected_book.id)
        self.assertEqual(book_from_dict.title, expected_book.title)
        self.assertEqual(book_from_dict.author, expected_book.author)
        self.assertEqual(book_from_dict.year, expected_book.year)
        self.assertEqual(book_from_dict.status, expected_book.status)


if __name__ == '__main__':
    unittest.main()
