"""Standalone script to populate Author and Book tables with famous names.

Usage: python seed_data.py
"""

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from library_app.models import Author, Book  # noqa: E402

AUTHORS = [
    ("Plato", 80),
    ("Aristotle", 62),
    ("Friedrich Nietzsche", 55),
    ("Immanuel Kant", 79),
    ("Jean-Paul Sartre", 74),
    ("Albert Camus", 46),
    ("Soren Kierkegaard", 42),
    ("Arthur Schopenhauer", 72),
    ("Fyodor Dostoevsky", 59),
    ("Leo Tolstoy", 82),
    ("William Shakespeare", 52),
    ("Jane Austen", 41),
    ("Franz Kafka", 40),
    ("George Orwell", 46),
    ("Virginia Woolf", 59),
    ("Gabriel Garcia Marquez", 87),
    ("Jorge Luis Borges", 86),
    ("Miguel de Cervantes", 68),
    ("Machado de Assis", 69),
    ("Fernando Pessoa", 47),
]

BOOKS = [
    ("The Republic", "Plato", -375),
    ("Symposium", "Plato", -385),
    ("Nicomachean Ethics", "Aristotle", -340),
    ("Metaphysics", "Aristotle", -350),
    ("Thus Spoke Zarathustra", "Friedrich Nietzsche", 1883),
    ("Beyond Good and Evil", "Friedrich Nietzsche", 1886),
    ("Critique of Pure Reason", "Immanuel Kant", 1781),
    ("Critique of Practical Reason", "Immanuel Kant", 1788),
    ("Being and Nothingness", "Jean-Paul Sartre", 1943),
    ("Nausea", "Jean-Paul Sartre", 1938),
    ("The Stranger", "Albert Camus", 1942),
    ("The Plague", "Albert Camus", 1947),
    ("Fear and Trembling", "Soren Kierkegaard", 1843),
    ("Either/Or", "Soren Kierkegaard", 1843),
    ("The World as Will and Representation", "Arthur Schopenhauer", 1818),
    ("On the Suffering of the World", "Arthur Schopenhauer", 1851),
    ("Crime and Punishment", "Fyodor Dostoevsky", 1866),
    ("The Brothers Karamazov", "Fyodor Dostoevsky", 1880),
    ("War and Peace", "Leo Tolstoy", 1869),
    ("Anna Karenina", "Leo Tolstoy", 1877),
    ("Hamlet", "William Shakespeare", 1600),
    ("Macbeth", "William Shakespeare", 1606),
    ("Pride and Prejudice", "Jane Austen", 1813),
    ("Sense and Sensibility", "Jane Austen", 1811),
    ("The Trial", "Franz Kafka", 1925),
    ("The Metamorphosis", "Franz Kafka", 1915),
    ("1984", "George Orwell", 1949),
    ("Animal Farm", "George Orwell", 1945),
    ("Mrs Dalloway", "Virginia Woolf", 1925),
    ("To the Lighthouse", "Virginia Woolf", 1927),
    ("One Hundred Years of Solitude", "Gabriel Garcia Marquez", 1967),
    ("Love in the Time of Cholera", "Gabriel Garcia Marquez", 1985),
    ("Ficciones", "Jorge Luis Borges", 1944),
    ("The Aleph", "Jorge Luis Borges", 1949),
    ("Don Quixote", "Miguel de Cervantes", 1605),
    ("Novelas ejemplares", "Miguel de Cervantes", 1613),
    ("Dom Casmurro", "Machado de Assis", 1899),
    ("The Posthumous Memoirs of Bras Cubas", "Machado de Assis", 1881),
    ("The Book of Disquiet", "Fernando Pessoa", 1982),
    ("Message", "Fernando Pessoa", 1934),
]


def run():
    authors_by_name = {}
    for name, age in AUTHORS:
        author, _ = Author.objects.get_or_create(name=name, defaults={"age": age})
        authors_by_name[name] = author

    for title, author_name, year in BOOKS:
        Book.objects.get_or_create(
            title=title,
            defaults={"author": authors_by_name[author_name], "publication_year": year},
        )

    print(f"Authors in database: {Author.objects.count()}")
    print(f"Books in database: {Book.objects.count()}")


if __name__ == "__main__":
    run()
