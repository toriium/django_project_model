from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.views import View


class BaseView(UserPassesTestMixin, View):
    def test_func(self):
        username = self.request.user.username
        path = self.request.path
        if username == "non_authorized_user" and "authors_table" not in path:
            raise PermissionDenied("User can't access this page")
        return True