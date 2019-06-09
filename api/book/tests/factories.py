from factory import DjangoModelFactory
from api.book.models.book import Book
from api.book.models.publisher import Publisher
from api.book.models.author import Author


class BookModelFactory(DjangoModelFactory):
    """
    Book Factory
    """
    class Meta:
        model = Book
    title = '978-4130620017'
    isbn = ''
    publisher = Publisher()
    author = Author()
    cover = ''
    publish_date = '2019'


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
