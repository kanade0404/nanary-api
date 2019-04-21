from users.models import User
from rest_framework import serializers


class AuthSerializer(serializers.ModelSerializer):
    """
    Authentication Serializer
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'display_username',
                  'icon_image', 'profile')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        """
        Sign up
        :param validated_data: a user info
        :return: a new user info
        """
        return User.objects.create_user(email=validated_data['email'],
                                        password=validated_data['password'],
                                        username=validated_data['username'])

    def update(self, instance, validated_data):
        pass


