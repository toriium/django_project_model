"""Standalone script to populate Author and Book tables with famous names.

Usage: python seed_data.py
"""

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

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
    {"title": "The Republic", "author": "Plato", "publication_year": -375, "genre": "Philosophy"},
    {"title": "Symposium", "author": "Plato", "publication_year": -385, "genre": "Philosophy"},
    {"title": "Nicomachean Ethics", "author": "Aristotle", "publication_year": -340, "genre": "Philosophy"},
    {"title": "Metaphysics", "author": "Aristotle", "publication_year": -350, "genre": "Philosophy"},
    {
        "title": "Thus Spoke Zarathustra",
        "author": "Friedrich Nietzsche",
        "publication_year": 1883,
        "genre": "Philosophy",
    },
    {"title": "Beyond Good and Evil", "author": "Friedrich Nietzsche", "publication_year": 1886, "genre": "Philosophy"},
    {"title": "Critique of Pure Reason", "author": "Immanuel Kant", "publication_year": 1781, "genre": "Philosophy"},
    {
        "title": "Critique of Practical Reason",
        "author": "Immanuel Kant",
        "publication_year": 1788,
        "genre": "Philosophy",
    },
    {"title": "Being and Nothingness", "author": "Jean-Paul Sartre", "publication_year": 1943, "genre": "Philosophy"},
    {"title": "Nausea", "author": "Jean-Paul Sartre", "publication_year": 1938, "genre": "Novel"},
    {"title": "The Stranger", "author": "Albert Camus", "publication_year": 1942, "genre": "Novel"},
    {"title": "The Plague", "author": "Albert Camus", "publication_year": 1947, "genre": "Novel"},
    {"title": "Fear and Trembling", "author": "Soren Kierkegaard", "publication_year": 1843, "genre": "Philosophy"},
    {"title": "Either/Or", "author": "Soren Kierkegaard", "publication_year": 1843, "genre": "Philosophy"},
    {
        "title": "The World as Will and Representation",
        "author": "Arthur Schopenhauer",
        "publication_year": 1818,
        "genre": "Philosophy",
    },
    {
        "title": "On the Suffering of the World",
        "author": "Arthur Schopenhauer",
        "publication_year": 1851,
        "genre": "Essay",
    },
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "publication_year": 1866, "genre": "Novel"},
    {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "publication_year": 1880, "genre": "Novel"},
    {"title": "War and Peace", "author": "Leo Tolstoy", "publication_year": 1869, "genre": "Novel"},
    {"title": "Anna Karenina", "author": "Leo Tolstoy", "publication_year": 1877, "genre": "Novel"},
    {"title": "Hamlet", "author": "William Shakespeare", "publication_year": 1600, "genre": "Tragedy"},
    {"title": "Macbeth", "author": "William Shakespeare", "publication_year": 1606, "genre": "Tragedy"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "publication_year": 1813, "genre": "Romance"},
    {"title": "Sense and Sensibility", "author": "Jane Austen", "publication_year": 1811, "genre": "Romance"},
    {"title": "The Trial", "author": "Franz Kafka", "publication_year": 1925, "genre": "Novel"},
    {"title": "The Metamorphosis", "author": "Franz Kafka", "publication_year": 1915, "genre": "Novella"},
    {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Dystopian"},
    {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945, "genre": "Satire"},
    {"title": "Mrs Dalloway", "author": "Virginia Woolf", "publication_year": 1925, "genre": "Novel"},
    {"title": "To the Lighthouse", "author": "Virginia Woolf", "publication_year": 1927, "genre": "Novel"},
    {
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel Garcia Marquez",
        "publication_year": 1967,
        "genre": "Magical Realism",
    },
    {
        "title": "Love in the Time of Cholera",
        "author": "Gabriel Garcia Marquez",
        "publication_year": 1985,
        "genre": "Romance",
    },
    {"title": "Ficciones", "author": "Jorge Luis Borges", "publication_year": 1944, "genre": "Short Stories"},
    {"title": "The Aleph", "author": "Jorge Luis Borges", "publication_year": 1949, "genre": "Short Stories"},
    {"title": "Don Quixote", "author": "Miguel de Cervantes", "publication_year": 1605, "genre": "Novel"},
    {
        "title": "Novelas ejemplares",
        "author": "Miguel de Cervantes",
        "publication_year": 1613,
        "genre": "Short Stories",
    },
    {"title": "Dom Casmurro", "author": "Machado de Assis", "publication_year": 1899, "genre": "Novel"},
    {
        "title": "The Posthumous Memoirs of Bras Cubas",
        "author": "Machado de Assis",
        "publication_year": 1881,
        "genre": "Novel",
    },
    {"title": "The Book of Disquiet", "author": "Fernando Pessoa", "publication_year": 1982, "genre": "Prose"},
    {"title": "Message", "author": "Fernando Pessoa", "publication_year": 1934, "genre": "Poetry"},
]


def run():
    countries_by_name = {}
    for data in COUNTRIES:
        country, _ = Country.objects.get_or_create(name=data["name"])
        countries_by_name[country.name] = country

    authors_by_name = {}
    for data in AUTHORS:
        author, _ = Author.objects.update_or_create(
            name=data["name"],
            defaults={**data, "country": countries_by_name[data["country"]]},
        )
        authors_by_name[author.name] = author

    for data in BOOKS:
        Book.objects.update_or_create(
            title=data["title"],
            defaults={**data, "author": authors_by_name[data["author"]]},
        )

    print(f"Countries in database: {Country.objects.count()}")
    print(f"Authors in database: {Author.objects.count()}")
    print(f"Books in database: {Book.objects.count()}")


if __name__ == "__main__":
    run()
