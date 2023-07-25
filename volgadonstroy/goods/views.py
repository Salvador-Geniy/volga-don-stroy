from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated


from goods.models import Good, Category
from goods.serializers import GoodSerializer


class CategoryViewSet(ListModelMixin, GenericViewSet):
    queryset = Category.objects.all().order_by('name')


class GoodViewSet(ListModelMixin, GenericViewSet):
    queryset = Good.objects.all().select_related('category').order_by('name')
    serializer_class = GoodSerializer


class GoodAdminViewSet(ModelViewSet):
    queryset = Good.objects.all().select_related('category').order_by('name')
    serializer_class = GoodSerializer
    permission_classes = [IsAuthenticated]

