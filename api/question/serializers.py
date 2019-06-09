from rest_framework import serializers
from .models import Question
from api.users.serializers import UserSerializer
from api.book.serializers.book import BookSerializer


class QuestionSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = UserSerializer()

    class Meta:
        model = Question
        fields = '__all__'
