from pydantic import BaseModel

from .shared_views import generate_static_table_html
from ..models import Author


def authors_table(request):
    class AuthorTable(BaseModel):
        name: str
        age: int

    authors = [
        AuthorTable(
            name=author.name,
            age=author.age,
        )
        for author in Author.objects.all()
    ]
    return generate_static_table_html(request, table_name="Authors", values=authors)
