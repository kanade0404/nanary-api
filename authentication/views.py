from logging import getLogger
from .filters import AuthFilter
from .serializers import AuthSerializer
from users.models import User
from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


logger = getLogger(__name__)


class AuthViewSet(viewsets.ModelViewSet):
    """
    Authentication ViewSet
    """
    queryset = User.objects.filter(is_active=True).order_by('-date_joined')
    serializer_class = AuthSerializer
    filter_class = AuthFilter

    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.create_user(email=request.data['email'],
                                            password=request.data['password'],
                                            username=request.data['username'])
            data = AuthSerializer(user).data
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.exception(f'Exception: {e}')
            return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        pass


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
        try:
            response = super(CustomAuthToken, self).post(request, *args, **kwargs)
            token = Token.objects.get(key=response.data['token'])
            user = User.objects.get(id=token.user_id)
            data = AuthSerializer(user, many=False).data
            return Response({'token': token.key, 'user': data}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(f'Exception: {e}')
            return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

