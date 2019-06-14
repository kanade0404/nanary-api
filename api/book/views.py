from logging import getLogger
from django.db import transaction
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from common.db.exception import RegisterError
from .openbd import OpenBD
# Models
from .models.book import Book
from .models.series import Series
# Serializers
from api.book.serializers.book import BookManagementSerializer
from api.book.serializers.book import BookSerializer
from api.book.serializers.publisher import PublisherSerializer
from api.book.serializers.author import AuthorSerializer
from api.book.serializers.series import SeriesSerializer
from api.book.serializers.series_book import SeriesBookSerializer

logger = getLogger(__name__)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        try:
            serializer = BookSerializer(data=request.data)
            if not serializer.is_valid():
                raise ValueError(serializer.errors)
            book = self.queryset
            serializer = BookSerializer(data=book)
            logger.info(serializer.data)
            return Response(data=serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logger.exception('Exception as BookViewSet.list')
            return Response(data={'error': e.args[0]}, status=HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass


class BookManagementView(ListCreateAPIView):
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
                logger.debug('Success BookManagementView.list')
                logger.debug(data)
                return Response(data=data, status=HTTP_200_OK)
            else:
                book = Book.objects.filter(isbn=request.data['isbn']).get()
                serializer = BookManagementSerializer(data=book)
                if not serializer.is_valid():
                    raise ValueError(serializer.errors)
                logger.debug('Success BookManagementView.list')
                logger.debug(serializer.data)
                return Response(data=serializer.data, status=HTTP_200_OK)
        except Exception as e:
            logger.error('Exception BookManagementView.list')
            logger.error(e)
            return Response(data={'error': e.args[0]}, status=HTTP_400_BAD_REQUEST)

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
            serializer = BookManagementSerializer(data=request.data)
            if not serializer.is_valid():
                raise ValueError(serializer.errors)
            # Publisher
            publisher_serializer = PublisherSerializer(data=serializer.validated_data)
            publisher_serializer.save()
            # Author
            author_serializer = AuthorSerializer(data=serializer.validated_data)
            author_serializer.save()
            # Book
            book_manage_serializer = BookManagementSerializer(data=serializer.validated_data)
            book_manage_serializer.save()
            # Series
            if serializer.validated_data['series'] != '':
                series = Series.objects.filter(name=serializer.validated_data['series']).get()
                if len(series) == 0:
                    series_serializer = SeriesSerializer(data=serializer.validated_data)
                    series_serializer.save()
                series_book_serializer = SeriesBookSerializer(data=serializer.validated_data)
                series_book_serializer.save()
            serializer = BookManagementSerializer(data=serializer.validated_data)
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        except RegisterError as e:
            logger.error('Exception BookManageViewSet.create')
            logger.error(e)
            return Response(data={'error': e.args[0]}, status=HTTP_400_BAD_REQUEST)
