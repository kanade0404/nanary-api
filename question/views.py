from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from common.db.exception import RegisterError
from .models import Question
from .serializers import QuestionSerializer
from book.models.book import Book
from users.models import User
from logging import getLogger

logger = getLogger(__name__)


class QuestionViewSet(viewsets.ViewSet):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer

    def list(self, request):
        try:
            question = Question.objects.all()
            return Response(question, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(f'Exception: {e}')
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        question = Question.objects.get(pk=pk)
        return Response(question, status=status.HTTP_200_OK)

    @transaction.atomic
    def create(self, request):
        try:
            question = Question(
                title=request.data['title'],
                content=request.data['content'],
                book=Book.objects.get(request.data['book']),
                user=User.objects.get(request.data['user'])
            )
            question.save()
            return Response(question, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(f'Exception: {e}')
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
