from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField(blank=True)
    document = models.FileField(
        upload_to='books/documents/', blank=True, null=True)

    def __str__(self):
        return self.title


class ReadingList(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reading_lists')
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(
        'Book', related_name='reading_lists', through='ReadingListItem')

    def __str__(self):
        return f"{self.user}'s Reading List - {self.name}"


class ReadingListItem(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    reading_list = models.ForeignKey(ReadingList, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(null=True)

    class Meta:
        unique_together = ('book', 'reading_list')

    def __str__(self):
        return f"{self.book} in {self.reading_list} at position {self.order}"
