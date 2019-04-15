from rest_framework import serializers
from book.models.book import Book
from .publisher import PublisherSerializer
from .author import AuthorSerializer


class BookManagementSerializer(serializers.ModelSerializer):
    """
    Book Management Serializer
    """
    publisher = PublisherSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('title', 'isbn', 'cover', 'publisher', 'author', 'publish_date')


class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('title', 'isbn', 'cover', 'publisher', 'author', 'publish_date')
