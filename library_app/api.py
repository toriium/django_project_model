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