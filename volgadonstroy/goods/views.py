import os

from django.conf import settings
from django.db import transaction
from django.http import Http404
from rest_framework import status
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import FormParser, MultiPartParser

from .models import Good, Category, Images
from .serializers import GoodSerializer, GoodCreateSerializer, \
    CategorySerializer, AlbumSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class GoodReadOnlyModeViewSet(ReadOnlyModelViewSet):
    """View for client side"""
    permission_classes = [AllowAny]
    queryset = Good.objects.filter(published=True).select_related('images')
    serializer_class = GoodSerializer


class GoodAdminView(ListModelMixin, GenericViewSet):
    """List view for admin side"""
    queryset = Good.objects.all().select_related(
        'category').select_related('images').order_by('name')
    serializer_class = GoodSerializer


class GoodCreateView(APIView):
    """View for create new Good object and related Images object"""
    parser_classes = [FormParser, MultiPartParser]
    serializer = GoodCreateSerializer

    @transaction.atomic
    def post(self, request, format=None):
        good_obj = None
        img1 = request.data.get('img1')
        img2 = request.data.get('img2')
        img3 = request.data.get('img3')
        img4 = request.data.get('img4')
        img5 = request.data.get('img5')

        serialized_data = self.serializer(data=request.data)

        if serialized_data.is_valid():
            good_obj = Good.objects.create(**serialized_data.validated_data)
            album_serialized_data = AlbumSerializer(data={
                'product': str(good_obj.id),
                'img1': img1,
                'img2': img2,
                'img3': img3,
                'img4': img4,
                'img5': img5,
            })
            if album_serialized_data.is_valid():
                Images.objects.create(**album_serialized_data.validated_data)
                response_data = self.serializer(Good.objects.last()).data
                return Response(data=response_data, status=status.HTTP_201_CREATED)
            return Response(AlbumSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(self.serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodDetailView(APIView):
    """View for get, update, delete Good object and related Images object"""
    parser_classes = [FormParser, MultiPartParser]

    def get_object(self, pk):
        try:
            return Good.objects.get(pk=pk)
        except Good.DoesNotExist:
            raise Http404

    def get_related_object(self, pk):
        good = Good.objects.get(pk=pk)
        return Images.objects.get_or_create(product=good)

    def get_image_list(self, obj):
        return [obj.img1, obj.img2, obj.img3, obj.img4, obj.img5]

    def delete_unused_images(self, images):
        for img in images:
            if img and os.path.exists(os.path.join(settings.MEDIA_ROOT, str(img))):
                os.remove(os.path.join(settings.MEDIA_ROOT, str(img)))

    def get(self, request, pk, format=None):
        obj = self.get_object(pk=pk)
        serializer = GoodSerializer(obj)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        good = self.get_object(pk=pk)
        album = self.get_related_object(pk=pk)
        old_images = self.get_image_list(obj=album)

        good_serialized_data = GoodSerializer(good, data=request.data, partial=True)
        album_serialized_data = AlbumSerializer(album, data=request.data, partial=True)
        if good_serialized_data.is_valid() and album_serialized_data.is_valid():
            good_serialized_data.save()
            album_serialized_data.save()
            new_images = self.get_image_list(album)

            images_for_delete = [old_images[i] for i in range(5) if old_images[i] != new_images[i]]
            self.delete_unused_images(images_for_delete)

            return Response(status=status.HTTP_200_OK)

        return Response({'detail': 'Not updated'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        good = self.get_object(pk=pk)
        old_images = self.get_image_list(good.images)
        good.delete()
        self.delete_unused_images(old_images)
        return Response(status=status.HTTP_204_NO_CONTENT)
