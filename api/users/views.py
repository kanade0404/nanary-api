from logging import getLogger
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from .filters import UserFilter

logger = getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True).order_by('-date_joined')
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    filter_class = UserFilter

    def list(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            user = self.queryset.get()
            serializer = self.serializer_class(user)
            return Response(serializer.data, HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'error': e.args[0]}, HTTP_400_BAD_REQUEST)


class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    filter_class = UserFilter

    def retrieve(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            user = self.queryset.get(pk=request.data['id'])
            serializer = self.serializer_class(user)
            return Response(serializer.data, HTTP_200_OK)
        except Exception as e:
            logger.exception(f'Exception: {e}')
            return Response({'error': e.args[0]}, status=HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            serializer = UserSerializer(request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            user = User.objects.get(pk=request.data['id'])
            if request.data['email']:
                user.email = request.data['email']
            if request.data['name']:
                user.name = request.data['name']
            if request.data['display_username']:
                user.display_username = request.data['display_username']
            if request.data['profile']:
                user.profile = request.data['profile']
            if request.data['icon_image']:
                user.icon_image = request.data['icon_image']
            user.date_updated = timezone.now
            user.save()
            data = UserSerializer(user).data
            return Response(data, status=HTTP_200_OK)
        except Exception as e:
            logger.exception(f'Exception: {e}')
            return Response({'error': e.args[0]}, status=HTTP_400_BAD_REQUEST)
