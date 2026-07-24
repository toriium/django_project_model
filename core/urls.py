from django.contrib import admin
from django.urls import path, include

from library_app.api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("", include("django.contrib.auth.urls")),
    path("", include("library_app.urls")),
]
