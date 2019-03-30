from django_filters import rest_framework as filters
from users.models import User


class AuthFilter(filters.FilterSet):
    """
    Authentication Filter
    """
    # email address
    email = filters.CharFilter(field_name='email', lookup_expr='exact')

    class Meta:
        model = User
        fields = ['email']
