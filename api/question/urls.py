from django.urls import path, include
from rest_framework import routers
from .views import QuestionViewSet

router = routers.DefaultRouter()
router.register('', QuestionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
