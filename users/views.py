from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from .filters import UserFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True).order_by('-date_joined')
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    filter_class = UserFilter
