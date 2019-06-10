from django.urls import path
from .views import UserViewSet, UserDetailViewSet

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'})),
    path('detail/', UserDetailViewSet.as_view({'get': 'retrieve'}))
]
