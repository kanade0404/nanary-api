from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from .models.author import Author
from .models.publisher import Publisher
from .models.book import Book
from .models.series import Series
from .models.series_book import SeriesBook
from book.serializers.book import BookManagementSerializer, BookSerializer
from .openbd import OpenBD
from .utils import BookUtil
from common.db.exception import RegisterError
from logging import getLogger

logger = getLogger(__name__)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

    class Meta:
        lookup_field = 'uuid'

    def list(self, request, *args, **kwargs):
        try:
            book = Book.objects.all()
            data = BookSerializer(book).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(f'Exception: {e.args[0]}')
            return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        pass


class BookManagementViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BookManagementSerializer

    class Meta:
        lookup_field = 'uuid'

    def list(self, request, *args, **kwargs):
        """
        Find book info from OpenBD API by ISBN Code.
        :param request: ISBN Code
        :param args:
        :param kwargs:
        :return: book info(format:json)
        """
        try:
            isbn = request.data['isbn'].replace('-', '')
            if Book.objects.filter(isbn=isbn).count() == 0:
                data = OpenBD().get_json(isbn)
                logger.debug('get book info from openbd api', data)
                return Response(data, status.HTTP_200_OK)
            else:
                book = Book.objects.filter(isbn=request.data['isbn']).get()
                data = BookManagementSerializer(instance=book).data
                logger.debug('get book info from db', data)
                return Response(data, status.HTTP_200_OK)
        except Exception as e:
            logger.exception(f'Exception as BookManagementViewSet.list: {e}')
            return Response({'error': e.args[0]}, status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        """
        create book info
        :param request: book info
        :param args:
        :param kwargs:
        :return: The registered book info if successful. Otherwise an error message
        """
        try:
            # is_create_*** is True if request.data has not been registered yet.
            # is_create_*** is False unless request.data has been registered.
            publisher, is_create_publisher = Publisher.objects.get_or_create(name=request.data['publisher'])
            author, is_create_author = Author.objects.get_or_create(name=request.data['author'])
            d = request.data['publish_date']
            book = Book(isbn=request.data['isbn'],
                        author=author,
                        title=request.data['title'],
                        publisher=publisher,
                        publish_date=BookUtil().pubdate_to_integer(d),
                        cover=request.data['cover'])
            book.save()
            if request.data['series'] != '':
                series = Series.objects.filter(name=request.data['series']).get()
                if len(series) == 0:
                    series = Series(name=request.data['series'])
                    series.save()
                series_book = SeriesBook(book_id=book, series_id=series)
                series_book.save()
            serializer = BookManagementSerializer(book)
            logger.debug('create ' * is_create_publisher + f'publisher:{publisher}')
            logger.debug('create ' * is_create_author + f'author: {author}')
            logger.debug(f'create book: {book}')
        except RegisterError as e:
            logger.exception(f'Exception at BookManageViewSet.create: {e}')
            return Response(e, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status.HTTP_201_CREATED)
