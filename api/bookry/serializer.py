from rest_framework import serializers
from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre']

class BookSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'rating', 'language', 'description', 'cover_image', 'started_reading', 'finished_reading', 'genres']

    def create(self, validated_data):
        genres_data = validated_data.pop('genres', [])
        book = Book.objects.create(**validated_data)
        for genre_data in genres_data:
            genre, created = Genre.objects.get_or_create(genre=genre_data['genre'])
            book.genres.add(genre)
        return book

    def update(self, instance, validated_data):
        genres_data = validated_data.pop('genres', [])
        
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.language = validated_data.get('language', instance.language)
        instance.description = validated_data.get('description', instance.description)
        instance.cover_image = validated_data.get('cover_image', instance.cover_image)
        instance.started_reading = validated_data.get('started_reading', instance.started_reading)
        instance.finished_reading = validated_data.get('finished_reading', instance.finished_reading)
        instance.save()
        
        instance.genres.clear()
        for genre_data in genres_data:
            genre, created = Genre.objects.get_or_create(genre=genre_data['genre'])
            instance.genres.add(genre)
        
        return instance