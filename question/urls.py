from django.urls import path, include
from rest_framework import routers
from .views import QuestionViewSet

router = routers.DefaultRouter()
router.register('', QuestionViewSet.as_view({'get': 'list'}))
router.register('detail', QuestionViewSet.as_view({'get': 'retrieve'}))

urlpatterns = [
    path('question/', include(router.urls))
]
