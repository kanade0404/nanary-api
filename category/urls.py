from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, CategoryTagViewSet

router = routers.DefaultRouter()
router.register('', CategoryViewSet)
router.register('tag', CategoryTagViewSet)

urlpatterns = [
    path('category/', include(router.urls)),
]
