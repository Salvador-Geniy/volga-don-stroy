from rest_framework.serializers import ModelSerializer

from goods.models import Good, Category, Images


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class GoodSerializer(ModelSerializer):
    category = CategorySerializer()
    images = AlbumSerializer()

    class Meta:
        model = Good
        fields = ('id', 'name', 'description', 'in_stock', 'published', 'category', 'images')


class GoodCreateSerializer(ModelSerializer):
    class Meta:
        model = Good
        fields = '__all__'

