from rest_framework import serializers
from book.models.publisher import Publisher


class PublisherSerializer(serializers.ModelSerializer):
    """
    Publisher Serializer
    """
    class Meta:
        model = Publisher
        fields = ('id', 'name')