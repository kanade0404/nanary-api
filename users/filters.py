from django_filters import rest_framework as filters
from .models import User


class UserFilter(filters.FilterSet):
    # メールアドレス完全一致
    email = filters.CharFilter(field_name='email', lookup_expr='exact')
    # ユーザー名部分一致
    username = filters.CharFilter(field_name='username', lookup_expr='contains')

    class Meta:
        model = User
        fields = ['email', 'username']
