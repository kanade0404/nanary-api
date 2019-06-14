from django.urls import path
from .views import BookManagementView, BookViewSet

urlpatterns = [
    path('', BookViewSet.as_view({'get': 'list'})),
    path('manage/', BookManagementView.as_view()),
]
