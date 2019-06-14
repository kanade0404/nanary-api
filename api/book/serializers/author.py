from logging import getLogger
from rest_framework import serializers
from api.book.models.author import Author
from rest_framework.validators import UniqueValidator


logger = getLogger(__name__)


class AuthorSerializer(serializers.ModelSerializer):
    """
    Author Serializer
    """
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Author.objects.all())]
    )

    class Meta:
        model = Author
        fields = ('id', 'name')

    def create(self, validated_data):
        author, is_created = Author.objects.get_or_create(name=validated_data['author'])
        logger.info('Success Author')
        logger.info(author)
        return author
