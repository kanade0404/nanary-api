from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from .models import Question
from .serializers import QuestionSerializer
from logging import getLogger

logger = getLogger(__name__)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs):
        try:
            question = self.queryset
            serializer = QuestionSerializer(question)
            logger.info('Success QuestionViewSet.list')
            logger.info(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error('Exception QuestionViewSet.list')
            logger.error(e)
            return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            question = self.queryset.get(pk=pk)
            serializer = QuestionSerializer(question)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            serializer = QuestionSerializer(data=request.data)
            if not serializer.is_valid():
                raise ValueError(serializer.errors)
            question = QuestionSerializer(data=serializer.validated_data)
            serializer = QuestionSerializer(question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.exception(f'Exception: {e}')
            return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
