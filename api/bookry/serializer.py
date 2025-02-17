from rest_framework import serializers
from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre']

class BookSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)  # Remove read_only=True to allow writing

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'rating', 'language', 'description', 'cover_image', 'started_reading', 'finished_reading', 'genres']

    def create(self, validated_data):
        # Extract the genres data from the validated data
        genres_data = validated_data.pop('genres', [])
        
        # Create the Book instance
        book = Book.objects.create(**validated_data)
        
        # Create Genre instances and associate them with the Book
        for genre_data in genres_data:
            Genre.objects.create(book=book, **genre_data)
        
        return book

    def update(self, instance, validated_data):
        # Extract the genres data from the validated data
        genres_data = validated_data.pop('genres', [])
        
        # Update the Book instance
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.language = validated_data.get('language', instance.language)
        instance.description = validated_data.get('description', instance.description)
        instance.cover_image = validated_data.get('cover_image', instance.cover_image)
        instance.started_reading = validated_data.get('started_reading', instance.started_reading)
        instance.finished_reading = validated_data.get('finished_reading', instance.finished_reading)
        instance.save()
        
        # Delete existing genres and create new ones
        instance.genres.all().delete()
        for genre_data in genres_data:
            Genre.objects.create(book=instance, **genre_data)
        
        return instance