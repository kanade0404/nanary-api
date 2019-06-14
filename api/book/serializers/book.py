from logging import getLogger
from rest_framework import serializers
from api.book.models.book import Book
from .publisher import PublisherSerializer
from .author import AuthorSerializer

logger = getLogger(__name__)


class BookManagementSerializer(serializers.ModelSerializer):
    """
    Book Management Serializer
    """
    publisher = PublisherSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('title', 'isbn', 'cover', 'publisher', 'author', 'publish_date')

    def create(self, validated_data):
        book = Book(
            isbn=validated_data['isbn'],
            author=validated_data['author'],
            title=validated_data['title'],
            publisher=validated_data['publisher'],
            publish_date=validated_data['publish_date'],
            cover=validated_data['cover']
        )
        book.save()
        logger.info('Success BookManagement.create')
        logger.info(book)
        return book


class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('title', 'isbn', 'cover', 'publisher', 'author', 'publish_date')

