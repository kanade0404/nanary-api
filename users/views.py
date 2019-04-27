from logging import getLogger
from django.utils import timezone
from rest_framework import viewsets, status
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
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(f'Exception: {e}')
            return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
