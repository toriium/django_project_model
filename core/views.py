from django.http import HttpRequest, JsonResponse


def health_check(request: HttpRequest):
    return JsonResponse({"status": "ok"})
