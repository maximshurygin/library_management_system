import uuid


class Book:
    """
    Класс, представляющий книгу в библиотечной системе.

    Атрибуты:
        id (str): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        status (str): Статус книги ("в наличии" или "выдана").
    """

    def __init__(self, title: str, author: str, year: int, id: str = None, status: str = "в наличии"):
        """
        Инициализирует экземпляр класса Book.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
            id (str, optional): Уникальный идентификатор книги. Если не указан, генерируется автоматически. По умолчанию None.
            status (str, optional): Статус книги. По умолчанию "в наличии".
        """

        self.id = id if id else str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __repr__(self):
        """
        Возвращает строковое представление объекта Book.

        Returns:
            str: Строковое представление книги.
        """

        return f"ID: {self.id}, название: {self.title}, автор: {self.author}, год издания: {self.year}, статус: {self.status}"

    def to_dict(self):
        """
        Преобразует объект Book в словарь.

        Returns:
            dict: Словарь с данными книги.
        """

        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Создает объект Book из словаря.

        Args:
            data (dict): Словарь с данными книги.

        Returns:
            Book: Экземпляр класса Book.
        """

        return Book(
            title=data["title"],
            author=data["author"],
            year=data["year"],
            id=data["id"],
            status=data["status"]
        )
