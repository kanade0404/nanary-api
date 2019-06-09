from django.urls import path
from .views import BookManagementViewSet, BookViewSet

urlpatterns = [
    path('', BookViewSet.as_view({'get': 'list'})),
    path('manage/', BookManagementViewSet.as_view({'get': 'list'})),
]
