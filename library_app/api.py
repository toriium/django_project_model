from datetime import datetime, timedelta
from math import ceil

from ninja import NinjaAPI, Schema
from ninja.security import django_auth

api = NinjaAPI()


@api.get("/test-fetch/", auth=django_auth)
def test_fetch(request):
    return {"text": "Text from API"}


class TextPayload(Schema):
    text: str


@api.post("/test-post/", auth=django_auth)
def test_post(request, payload: TextPayload):
    return {"text": payload.text}


@api.get("/authors/", auth=django_auth)
def authors_list(request, page: int = 1, size: int = 15):
    last_page = max(1, ceil(len(AUTHORS) / size))
    start = (page - 1) * size
    return {"data": AUTHORS[start : start + size], "last_page": last_page}