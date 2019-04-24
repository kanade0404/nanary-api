from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category, CategoryTag
from .serializers import CategorySerializer, CategoryTagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer


class CategoryTagViewSet(viewsets.ModelViewSet):
    queryset = CategoryTag.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CategoryTagSerializer
