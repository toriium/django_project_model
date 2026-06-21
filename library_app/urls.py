from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("people/", views.people_table, name="people_table"),
    path("public/", views.public, name="public"),
    path("test/404/", views.trigger_404, name="trigger_404"),
    path("test/500/", views.trigger_500, name="trigger_500"),
]
