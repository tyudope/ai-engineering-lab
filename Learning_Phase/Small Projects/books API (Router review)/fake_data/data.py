from typing import Optional
from model.book import Book

_books = [
    Book(id = 1, name = "Thinking Fast and Slow" , category="Psychology", pages = 705),
    Book(id = 2, name = "Lord of the Rings : Return of the king" , category= "Fantasy", pages = 700),
    Book(id = 3, name = "I, Robot", category = "Sci-Fi" , pages = 350),
    Book(id = 4, name = "Foundation", category="Sci-Fi" , pages = 700)
]


def get_all() -> list[Book]:
    """Return all books."""
    return _books


def get_one(name : str) -> Optional[Book]:
    """Return only one book with given name"""
    for book in _books:
        if book.name == name:
            return book
    return None

def get_by_category(category: str) -> list[Book]:
    """Return books by category."""
    books = [book for book in _books if book.category == category]
    if books is None or len(books) == 0:
        return None
    return books


