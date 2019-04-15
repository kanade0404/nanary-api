from django.urls import path, include
from rest_framework import routers
from .views import CommentViewSet

router = routers.DefaultRouter()
router.register('', CommentViewSet.as_view({'get': 'list'}))
router.register('detail', CommentViewSet.as_view({'get': 'retrieve'}))

urlpatterns = [
    path('comment/', include(router.urls))
]
