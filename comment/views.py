from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from .models import Comment
from .serializers import CommentSerializer
from users.models import User
from question.models import Question
from logging import getLogger


logget = getLogger(__name__)


class CommentViewSet(viewsets.ViewSet):
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def list(self, request):
        comment = Comment.objects.all()
        return Response(comment, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        comment = Comment.objects.get(pk=pk)
        return Response(comment, status=status.HTTP_200_OK)

    @transaction.atomic
    def create(self, request):
        try:
            comment = Comment(
                content=request.data['content'],
                user=User.objects.get(request.data['user']),
                question=Question.objects.get(request.data['question'])
            )
            comment.save()
            return Response(comment, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

