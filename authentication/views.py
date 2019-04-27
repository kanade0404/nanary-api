from logging import getLogger
from django.db import transaction
from .filters import AuthFilter
from .serializers import AuthSerializer
from users.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

logger = getLogger(__name__)


class AuthViewSet(viewsets.ModelViewSet):
    """
    Authentication ViewSet
    """
    permission_classes = (AllowAny,)
    queryset = User.objects.filter(is_active=True).order_by('-date_joined')
    serializer_class = AuthSerializer
    filter_class = AuthFilter

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            serializer = AuthSerializer(data=request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.exception('Exception')
            return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
