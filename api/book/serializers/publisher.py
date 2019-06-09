from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from api.book.models.publisher import Publisher


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
