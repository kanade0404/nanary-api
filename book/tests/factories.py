from factory import DjangoModelFactory
from book.models import Book, Publisher, Author


class BookModelFactory(DjangoModelFactory):
    """
    Book Factory
    """
    class Meta:
        model = Book
    title = ''
    isbn = ''
    publisher = Publisher()
    author = Author()
    cover = ''
    publish_date = 000000


class PublisherModelFactory(DjangoModelFactory):
    """
    Publisher Factory
    """
    class Meta:
        model = Publisher
    name = ''


class AuthorModelFactory(DjangoModelFactory):
    """
    Author Factory
    """
    class Meta:
        model = Author
    name = ''
