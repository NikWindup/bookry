from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=100, null=True)
    rating = models.PositiveSmallIntegerField(null=True)
    language = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    cover_image = models.ImageField(null=True)
    started_reading = models.DateTimeField(auto_now_add=True, null=True)
    finished_reading = models.DateTimeField(blank=True, null=True)
    
    
class Genre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, related_name='genres')
    genre = models.CharField(max_length=50, unique=True, null=True)
