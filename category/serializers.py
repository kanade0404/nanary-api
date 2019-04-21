from rest_framework import serializers
from .models import Category, CategoryTag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryTagSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = CategoryTag
        fields = '__all__'
