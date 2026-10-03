from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Country(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, related_name="authors")

    def __str__(self):
        return self.name

    class Meta:
        managed = True


class Book(BaseModel):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="books")
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.title} ({self.author})"

    class Meta:
        managed = True
