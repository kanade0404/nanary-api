from logging import getLogger
from django.db import transaction
from .serializers import AuthSerializer
from api.users.models import User
from rest_framework import generics
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED,HTTP_400_BAD_REQUEST
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
        try:
            serializer = AuthSerializer(instance=request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            data = serializer.validated_data
            user = User.objects.create_user(
                email=request.data['email'],
                password=request.data['password'],
                username=request.data['username']
            )
            serializer = AuthSerializer(instance=user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            logger.exception('Exception')
            return Response({'error': e.args[0]}, status=HTTP_400_BAD_REQUEST)
