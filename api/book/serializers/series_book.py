from logging import getLogger
from rest_framework import serializers
from api.book.models.series_book import SeriesBook
from api.book.serializers.book import BookSerializer
from api.book.serializers.series import SeriesSerializer

logger = getLogger(__name__)


class SeriesBookSerializer(serializers.ModelSerializer):
    series = SeriesSerializer()
    book = BookSerializer()

    class Meta:
        model = SeriesBook
        fields = ('book', 'series')

    def create(self, validated_data):
        series_book = SeriesBook(
            book=validated_data['book'],
            series=validated_data['series']
        )
        series_book.save()
        logger.info('SeriesBook')
        logger.info(series_book)
        return series_book
