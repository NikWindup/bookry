from django.db import models


# Create your models here.
class Book(models.Model):
    
    GENRE_CHOICES = [
        ('FIC', 'Fiction'),
        ('NON', 'Non-Fiction'),
        ('SCI', 'Science'),
        ('HIS', 'History'),
        ('BIO', 'Biography'),
        ('FAN', 'Fantasy'),
        ('THR', 'Thriller'),
        ('ROM', 'Romance'),
        ('HOR', 'Horror'),
        ('OTH', 'Other'),
    ]
    
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES, default='OTH')
    rating = models.PositiveSmallIntegerField()
    language = models.CharField(max_length=50)
    description = models.TextField()
    cover_image = models.ImageField()
    
    def __str__(self):
        return f"{self.title} by {self.author}"