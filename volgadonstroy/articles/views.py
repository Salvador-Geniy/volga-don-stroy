import os

from django.core.cache import cache
from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny

from common_services.cache_service import get_data_from_cache_or_queryset
from volgadonstroy import settings

from .models import Article
from .serializers import ArticleSerializer


class ArticleReadOnlyModelViewSet(ReadOnlyModelViewSet):
    """Client side list view"""
    permission_classes = [AllowAny]
    queryset = Article.objects.filter(published=True).order_by('-created_at')
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        goods_cache_name = 'articles'

        serializer_data = get_data_from_cache_or_queryset(
            object=self,
            object_cache_name=goods_cache_name
        )
        return Response(serializer_data)


class ArticleListView(generics.ListCreateAPIView):
    """Admin side list and new article create view"""
    parser_classes = [MultiPartParser, FormParser]
    queryset = Article.objects.all().order_by('created_at')
    serializer_class = ArticleSerializer


class ArticleDetailView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        old_img = article.image
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            try:
                if serializer.validated_data['image'] != old_img:
                    if os.path.exists(os.path.join(settings.MEDIA_ROOT, str(old_img))):
                        os.remove(os.path.join(settings.MEDIA_ROOT, str(old_img)))
                serializer.save()
            except ValueError:
                return Response({'detail': 'Serializer is not valid.'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'detail': 'Updated.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        old_img = article.image
        article.delete()
        if os.path.exists(os.path.join(settings.MEDIA_ROOT, str(old_img))):
            os.remove(os.path.join(settings.MEDIA_ROOT, str(old_img)))
        return Response(status=status.HTTP_204_NO_CONTENT)
