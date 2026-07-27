import math
from typing import List

from ninja import NinjaAPI, Schema
from ninja.security import django_auth

from library_app.models import Author

api = NinjaAPI()


@api.get("/test-fetch/", auth=django_auth)
def test_fetch(request):
    return {"text": "Text from API"}


class TextPayload(Schema):
    text: str

class TableSchema(Schema):
    columns: List[str]
    rows: List[dict]
    limit: int
    offset: int
    qtd_pages: int


def build_response_table(table, limit: int, offset: int) -> TableSchema:
    qtd_all_rows = table.objects.count()
    columns = [field.name for field in table._meta.fields]
    rows = list(table.objects.all()[offset:offset + limit].values())
    qtd_pages = math.ceil(qtd_all_rows / limit)

    return TableSchema(
        columns=columns,
        rows=rows,
        limit=limit,
        offset=offset,
        qtd_pages=qtd_pages
    )



@api.post("/test-post/", auth=django_auth)
def test_post(request, payload: TextPayload):
    return {"text": payload.text}


@api.get("/authors", response=TableSchema)
def list_authors(request, limit: int = 10, offset: int = 0):
    return build_response_table(table=Author, limit=limit, offset=offset)
