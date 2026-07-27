from pydantic import BaseModel

from .shared_views import generate_generic_table
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
    return generate_generic_table(request, table_name="Authors", values=authors)
