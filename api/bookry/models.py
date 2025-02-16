from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    pages = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, default='English')
    cover_image = models.URLField(blank=True, null=True)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length=50)

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        default=1
    )
