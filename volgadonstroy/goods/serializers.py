from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from goods.models import Good, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class GoodSerializer(ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Good
        fields = ('category_name', 'name', 'description', 'image')

