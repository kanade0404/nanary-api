from django.urls import path, include
from rest_framework import routers
from .views import BookManagementViewSet, BookViewSet

router = routers.DefaultRouter()
router.register('', BookViewSet)
router.register('manage', BookManagementViewSet, base_name='manage')

urlpatterns = [
    path('book/', include(router.urls))
]
