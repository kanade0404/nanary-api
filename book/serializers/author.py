from rest_framework import serializers
from book.models.author import Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    Author Serializer
    """
    class Meta:
        model = Author
        fields = ('id', 'name')
