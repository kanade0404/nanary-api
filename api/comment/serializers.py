from rest_framework import serializers
from .models import Comment
from api.question.serializers import QuestionSerializer
from api.users.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    question = QuestionSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
