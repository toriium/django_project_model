from datetime import datetime

from pydantic import BaseModel

from .shared_views import generate_static_table_html
from ..models import Book


def books_table(request):
    class BookTable(BaseModel):
        title: str
        author: str
        publication_year: int
        created_at: datetime

    books = [
        BookTable(
            title=book.title,
            author=book.author.name,
            publication_year=book.publication_year,
            created_at=book.created_at,
        )
        for book in Book.objects.select_related("author").all()
    ]
    return generate_static_table_html(request, table_name="Books", values=books)
