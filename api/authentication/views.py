from logging import getLogger
from django.db import transaction
from .serializers import AuthSerializer
from api.users.models import User
from rest_framework import generics
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

logger = getLogger(__name__)


class AuthAPIView(generics.CreateAPIView):
    """
    Authentication ViewSet
    """
    permission_classes = (AllowAny,)
    queryset = User.objects.filter(is_active=True)
    serializer_class = AuthSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        """
        TODO
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            serializer = AuthSerializer(data=request.data)
            if not serializer.is_valid():
                raise ValueError(serializer.errors)
            user = serializer.save()
            serializer = AuthSerializer(data=user)
            logger.info('Success AuthAPIView')
            logger.info(serializer.data)
            return Response(serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            logger.error('Exception AuthAPIView')
            logger.error(e)
            return Response({'error': e.args[0]}, status=HTTP_400_BAD_REQUEST)
