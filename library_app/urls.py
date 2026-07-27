from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("people/", views.people_table, name="people_table"),
    path("books/", views.books_table, name="books_table"),
    path("multi_table/", views.multi_table, name="multi_table"),
    path("public/", views.public, name="public"),
    path("test-fetch/", views.test_fetch, name="test_fetch"),
    path("test-post/", views.test_post, name="test_post"),
    path("authors/", views.authors_table, name="authors_table"),
    path("test/404/", views.trigger_404, name="trigger_404"),
    path("test/500/", views.trigger_500, name="trigger_500"),
]
