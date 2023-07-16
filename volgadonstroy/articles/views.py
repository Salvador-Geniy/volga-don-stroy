from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticleViewSet(ListModelMixin, GenericViewSet):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer
