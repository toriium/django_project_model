import math

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
    limit: int
    offset: int
    qtd_pages: int
    columns: list[str]
    rows: list[dict]


def build_model_response_table(table, limit: int, offset: int, fields: list[str]) -> TableSchema:
    qtd_all_rows = table.objects.count()
    qtd_pages = math.ceil(qtd_all_rows / limit)

    # Fields that will be displayed in the table
    remove_fields = ["id", "created_at", "updated_at"]
    all_fields = [field.name for field in table._meta.fields]
    columns = fields if fields else all_fields
    columns = [column for column in columns if column not in remove_fields]

    rows = list(table.objects.all()[offset:offset + limit].values(*columns))

    return TableSchema(
        limit=limit,
        offset=offset,
        qtd_pages=qtd_pages,
        columns=columns,
        rows=rows,
    )



@api.post("/test-post/", auth=django_auth)
def test_post(request, payload: TextPayload):
    return {"text": payload.text}


@api.get("/authors", response=TableSchema)
def list_authors(request, limit: int = 10, offset: int = 0):
    return build_model_response_table(table=Author, limit=limit, offset=offset, fields=[])
