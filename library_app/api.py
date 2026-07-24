from ninja import NinjaAPI
from ninja.security import django_auth

api = NinjaAPI()


@api.get("/test-fetch/", auth=django_auth)
def test_fetch(request):
    return {"text": "Text from API"}