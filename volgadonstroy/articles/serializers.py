from rest_framework.serializers import ModelSerializer, Serializer

from articles.models import Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
