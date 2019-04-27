from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'display_username', 'email',
                  'profile', 'icon_image', 'date_joined', 'date_updated')
