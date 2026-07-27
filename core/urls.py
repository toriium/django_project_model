from django.contrib import admin
from django.urls import path, include

from library_app.api import api
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("health_check/", views.health_check, name="health_check"),
    path("", include("django.contrib.auth.urls")),
    path("", include("library_app.urls")),
]
