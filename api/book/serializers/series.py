from logging import getLogger
from api.book.models.series import Series
from rest_framework import serializers

logger = getLogger(__name__)


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('id', 'name')

    def create(self, validated_data):
        """
        Create series data.
        :param validated_data:
        :return:
        """
        series = Series(id=validated_data['id'], name=validated_data['name'])
        series.save()
        logger.info('Success Series')
        logger.info(series)
        return series
