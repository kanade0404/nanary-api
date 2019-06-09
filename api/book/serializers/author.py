from rest_framework import serializers
from api.book.models.author import Author
from rest_framework.validators import UniqueValidator


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
