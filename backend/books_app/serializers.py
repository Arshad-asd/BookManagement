from rest_framework import serializers
from .models import *
from django.core.exceptions import ObjectDoesNotExist


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    authors = serializers.CharField(required=True)
    genre = serializers.CharField(required=True)
    publication_date = serializers.DateField(required=True)
    document = serializers.FileField(required=True)
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Book
        fields = ['id', 'user', 'title', 'authors', 'genre',
                  'publication_date', 'description', 'document',]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        book = Book.objects.create(**validated_data)
        return book


class ReadingListSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Book.objects.all())

    class Meta:
        model = ReadingList
        fields = ['id', 'name', 'books']

    def create(self, validated_data):
        user = self.context['request'].user
        books_data = validated_data.pop('books')
        reading_list = ReadingList.objects.create(user=user, **validated_data)
        for book in books_data:
            ReadingListItem.objects.create(
                reading_list=reading_list, book=book)
        return reading_list


class AddBookToReadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingListItem
        fields = ['book']
