from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from .models import Comment
from .serializers import CommentSerializer
from users.models import User
from question.models import Question
from logging import getLogger


logger = getLogger(__name__)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        try:
            comment = self.queryset.get()
            data = CommentSerializer(comment).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(f'Exception: {e}')
            return Response({'error': e.args[0]})

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            comment = Comment.objects.get(pk=pk)
            data = CommentSerializer(comment).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(f'Exception: {e}')
            return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            serializer = CommentSerializer(data=request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            comment = Comment(
                content=serializer.validated_data['content'],
                user=User.objects.get(pk=int(serializer.validated_data['user'])),
                question=Question.objects.get(pk=int(serializer.validated_data['question']))
            )
            comment.save()
            data = CommentSerializer(comment).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(f'Exception: {e}')
            return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

