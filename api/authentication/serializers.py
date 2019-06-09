from api.users.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class AuthSerializer(serializers.ModelSerializer):
    """
    Authentication Serializer
    """
    username = serializers.CharField(max_length=50, validators=[
        UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(min_length=8, read_only=True)
    display_username = serializers.CharField(required=False)
    icon_image = serializers.ImageField(required=False)
    profile = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'display_username',
                  'icon_image', 'profile')
        extra_kwargs = {
            'username': {
                'error_messages': {'blank': 'ユーザー名は必須です。'}
            },
            'email': {
                'error_messages': {'blank': 'メールアドレスは必須です。'}
            },
            'password': {
                'error_messages': {'blank': 'パスワードは必須です。'}
            }
        }
