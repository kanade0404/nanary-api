from logging import getLogger
from rest_framework import serializers
from .models import Question
from api.users.serializers import UserSerializer
from api.book.serializers.book import BookSerializer
from api.book.models.book import Book
from api.users.models import User

logger = getLogger(__name__)


class QuestionSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = UserSerializer()

    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):
        question = Question(
            title=validated_data['title'],
            content=validated_data['content'],
            book=User.objects.get(pk=int(validated_data['book'])),
            user=User.objects.get(pk=int(validated_data['user']))
        )
        question.save()
        logger.info('Success Question')
        logger.info(question)
        return question
