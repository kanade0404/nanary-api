from logging import getLogger
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from api.book.models.publisher import Publisher

logger = getLogger(__name__)


class PublisherSerializer(serializers.ModelSerializer):
    """
    Publisher Serializer
    """
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Publisher.objects.all())]
    )

    class Meta:
        model = Publisher
        fields = ('id', 'name')

    def create(self, validated_data):
        publisher, is_created = Publisher.objects.get_or_create(name=validated_data['publisher'])
        logger.info('Success Publisher')
        logger.info(publisher)
        return publisher
