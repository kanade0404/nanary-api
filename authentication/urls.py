from django.urls import path, include
from rest_framework import routers
from .views import AuthViewSet, CustomAuthToken

router = routers.DefaultRouter()
router.register('', AuthViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth-token/', CustomAuthToken.as_view()),
]
