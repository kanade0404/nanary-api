from .filters import AuthFilter
from .serializers import AuthSerializer
from users.serializers import UserSerializer
from users.models import User
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class AuthViewSet(viewsets.ModelViewSet):
    """
    Authentication ViewSet
    """
    queryset = User.objects.filter(is_active=True).order_by('-date_joined')
    serializer_class = AuthSerializer
    filter_class = AuthFilter


class CustomAuthToken(ObtainAuthToken):
    """
    Token Authentication ViewSet
    """
    def post(self, request, *args, **kwargs):
        """
        Token Authentication
        :param request: user info
        :param args: other args
        :param kwargs: extra args
        :return: token and user info
        """
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        serializer = UserSerializer(user, many=False)
        return Response({'token': token.key, 'user': serializer.data})
