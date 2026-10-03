"""Standalone script that wipes and repopulates the Country, Author and Book tables with famous names.

Usage: python seed_data.py
"""

import os
from datetime import date

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.db import transaction  # noqa: E402

from library_app.models import Author, Book, Country  # noqa: E402

COUNTRIES = [
    {"name": "Greece"},
    {"name": "Germany"},
    {"name": "France"},
    {"name": "Denmark"},
    {"name": "Russia"},
    {"name": "England"},
    {"name": "Czech Republic"},
    {"name": "Colombia"},
    {"name": "Argentina"},
    {"name": "Spain"},
    {"name": "Brazil"},
    {"name": "Portugal"},
]

AUTHORS = [
    {"name": "Plato", "age": 80, "country": "Greece"},
    {"name": "Aristotle", "age": 62, "country": "Greece"},
    {"name": "Friedrich Nietzsche", "age": 55, "country": "Germany"},
    {"name": "Immanuel Kant", "age": 79, "country": "Germany"},
    {"name": "Jean-Paul Sartre", "age": 74, "country": "France"},
    {"name": "Albert Camus", "age": 46, "country": "France"},
    {"name": "Soren Kierkegaard", "age": 42, "country": "Denmark"},
    {"name": "Arthur Schopenhauer", "age": 72, "country": "Germany"},
    {"name": "Fyodor Dostoevsky", "age": 59, "country": "Russia"},
    {"name": "Leo Tolstoy", "age": 82, "country": "Russia"},
    {"name": "William Shakespeare", "age": 52, "country": "England"},
    {"name": "Jane Austen", "age": 41, "country": "England"},
    {"name": "Franz Kafka", "age": 40, "country": "Czech Republic"},
    {"name": "George Orwell", "age": 46, "country": "England"},
    {"name": "Virginia Woolf", "age": 59, "country": "England"},
    {"name": "Gabriel Garcia Marquez", "age": 87, "country": "Colombia"},
    {"name": "Jorge Luis Borges", "age": 86, "country": "Argentina"},
    {"name": "Miguel de Cervantes", "age": 68, "country": "Spain"},
    {"name": "Machado de Assis", "age": 69, "country": "Brazil"},
    {"name": "Fernando Pessoa", "age": 47, "country": "Portugal"},
]

BOOKS = [
    {"title": "The Republic", "author": "Plato", "publication_year": -375, "genre": "Philosophy", "published_at": None},
    {"title": "Symposium", "author": "Plato", "publication_year": -385, "genre": "Philosophy", "published_at": None},
    {
        "title": "Nicomachean Ethics",
        "author": "Aristotle",
        "publication_year": -340,
        "genre": "Philosophy",
        "published_at": None,
    },
    {
        "title": "Metaphysics",
        "author": "Aristotle",
        "publication_year": -350,
        "genre": "Philosophy",
        "published_at": None,
    },
    {
        "title": "Thus Spoke Zarathustra",
        "author": "Friedrich Nietzsche",
        "publication_year": 1883,
        "genre": "Philosophy",
        "published_at": date(1883, 1, 1),
    },
    {
        "title": "Beyond Good and Evil",
        "author": "Friedrich Nietzsche",
        "publication_year": 1886,
        "genre": "Philosophy",
        "published_at": date(1886, 1, 1),
    },
    {
        "title": "Critique of Pure Reason",
        "author": "Immanuel Kant",
        "publication_year": 1781,
        "genre": "Philosophy",
        "published_at": date(1781, 1, 1),
    },
    {
        "title": "Critique of Practical Reason",
        "author": "Immanuel Kant",
        "publication_year": 1788,
        "genre": "Philosophy",
        "published_at": date(1788, 1, 1),
    },
    {
        "title": "Being and Nothingness",
        "author": "Jean-Paul Sartre",
        "publication_year": 1943,
        "genre": "Philosophy",
        "published_at": date(1943, 1, 1),
    },
    {
        "title": "Nausea",
        "author": "Jean-Paul Sartre",
        "publication_year": 1938,
        "genre": "Novel",
        "published_at": date(1938, 1, 1),
    },
    {
        "title": "The Stranger",
        "author": "Albert Camus",
        "publication_year": 1942,
        "genre": "Novel",
        "published_at": date(1942, 1, 1),
    },
    {
        "title": "The Plague",
        "author": "Albert Camus",
        "publication_year": 1947,
        "genre": "Novel",
        "published_at": date(1947, 1, 1),
    },
    {
        "title": "Fear and Trembling",
        "author": "Soren Kierkegaard",
        "publication_year": 1843,
        "genre": "Philosophy",
        "published_at": date(1843, 10, 16),
    },
    {
        "title": "Either/Or",
        "author": "Soren Kierkegaard",
        "publication_year": 1843,
        "genre": "Philosophy",
        "published_at": date(1843, 2, 20),
    },
    {
        "title": "The World as Will and Representation",
        "author": "Arthur Schopenhauer",
        "publication_year": 1818,
        "genre": "Philosophy",
        "published_at": date(1818, 1, 1),
    },
    {
        "title": "On the Suffering of the World",
        "author": "Arthur Schopenhauer",
        "publication_year": 1851,
        "genre": "Essay",
        "published_at": date(1851, 1, 1),
    },
    {
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "publication_year": 1866,
        "genre": "Novel",
        "published_at": date(1866, 1, 1),
    },
    {
        "title": "The Brothers Karamazov",
        "author": "Fyodor Dostoevsky",
        "publication_year": 1880,
        "genre": "Novel",
        "published_at": date(1880, 1, 1),
    },
    {
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "publication_year": 1869,
        "genre": "Novel",
        "published_at": date(1869, 1, 1),
    },
    {
        "title": "Anna Karenina",
        "author": "Leo Tolstoy",
        "publication_year": 1877,
        "genre": "Novel",
        "published_at": date(1877, 1, 1),
    },
    {
        "title": "Hamlet",
        "author": "William Shakespeare",
        "publication_year": 1600,
        "genre": "Tragedy",
        "published_at": date(1600, 1, 1),
    },
    {
        "title": "Macbeth",
        "author": "William Shakespeare",
        "publication_year": 1606,
        "genre": "Tragedy",
        "published_at": date(1606, 1, 1),
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publication_year": 1813,
        "genre": "Romance",
        "published_at": date(1813, 1, 28),
    },
    {
        "title": "Sense and Sensibility",
        "author": "Jane Austen",
        "publication_year": 1811,
        "genre": "Romance",
        "published_at": date(1811, 10, 30),
    },
    {
        "title": "The Trial",
        "author": "Franz Kafka",
        "publication_year": 1925,
        "genre": "Novel",
        "published_at": date(1925, 4, 26),
    },
    {
        "title": "The Metamorphosis",
        "author": "Franz Kafka",
        "publication_year": 1915,
        "genre": "Novella",
        "published_at": date(1915, 1, 1),
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "publication_year": 1949,
        "genre": "Dystopian",
        "published_at": date(1949, 6, 8),
    },
    {
        "title": "Animal Farm",
        "author": "George Orwell",
        "publication_year": 1945,
        "genre": "Satire",
        "published_at": date(1945, 8, 17),
    },
    {
        "title": "Mrs Dalloway",
        "author": "Virginia Woolf",
        "publication_year": 1925,
        "genre": "Novel",
        "published_at": date(1925, 5, 14),
    },
    {
        "title": "To the Lighthouse",
        "author": "Virginia Woolf",
        "publication_year": 1927,
        "genre": "Novel",
        "published_at": date(1927, 5, 5),
    },
    {
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel Garcia Marquez",
        "publication_year": 1967,
        "genre": "Magical Realism",
        "published_at": date(1967, 5, 30),
    },
    {
        "title": "Love in the Time of Cholera",
        "author": "Gabriel Garcia Marquez",
        "publication_year": 1985,
        "genre": "Romance",
        "published_at": date(1985, 1, 1),
    },
    {
        "title": "Ficciones",
        "author": "Jorge Luis Borges",
        "publication_year": 1944,
        "genre": "Short Stories",
        "published_at": date(1944, 1, 1),
    },
    {
        "title": "The Aleph",
        "author": "Jorge Luis Borges",
        "publication_year": 1949,
        "genre": "Short Stories",
        "published_at": date(1949, 1, 1),
    },
    {
        "title": "Don Quixote",
        "author": "Miguel de Cervantes",
        "publication_year": 1605,
        "genre": "Novel",
        "published_at": date(1605, 1, 16),
    },
    {
        "title": "Novelas ejemplares",
        "author": "Miguel de Cervantes",
        "publication_year": 1613,
        "genre": "Short Stories",
        "published_at": date(1613, 1, 1),
    },
    {
        "title": "Dom Casmurro",
        "author": "Machado de Assis",
        "publication_year": 1899,
        "genre": "Novel",
        "published_at": date(1899, 1, 1),
    },
    {
        "title": "The Posthumous Memoirs of Bras Cubas",
        "author": "Machado de Assis",
        "publication_year": 1881,
        "genre": "Novel",
        "published_at": date(1881, 1, 1),
    },
    {
        "title": "The Book of Disquiet",
        "author": "Fernando Pessoa",
        "publication_year": 1982,
        "genre": "Prose",
        "published_at": date(1982, 1, 1),
    },
    {
        "title": "Message",
        "author": "Fernando Pessoa",
        "publication_year": 1934,
        "genre": "Poetry",
        "published_at": date(1934, 1, 1),
    },
]


@transaction.atomic
def run():
    # Delete in dependency order, since the foreign keys are PROTECT
    Book.objects.all().delete()
    Author.objects.all().delete()
    Country.objects.all().delete()

    countries_by_name = {}
    for data in COUNTRIES:
        countries_by_name[data["name"]] = Country.objects.create(**data)

    authors_by_name = {}
    for data in AUTHORS:
        authors_by_name[data["name"]] = Author.objects.create(**{**data, "country": countries_by_name[data["country"]]})

    for data in BOOKS:
        Book.objects.create(**{**data, "author": authors_by_name[data["author"]]})

    print(f"Countries in database: {Country.objects.count()}")
    print(f"Authors in database: {Author.objects.count()}")
    print(f"Books in database: {Book.objects.count()}")


if __name__ == "__main__":
    run()
