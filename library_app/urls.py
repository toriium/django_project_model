from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("people/", views.people_table, name="people_table"),
]
