from django.core.exceptions import PermissionDenied

ALLOWED_PATHS_FOR_USER = ("/", "/authors/", "/api/authors")


class RestrictNonAuthorizedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated and user.username == "non_authorized_user":
            if request.path not in ALLOWED_PATHS_FOR_USER:
                raise PermissionDenied("User can't access this page.")
        return self.get_response(request)