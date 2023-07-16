from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from goods.models import Good
from goods.serializers import GoodSerializer


class GoodViewSet(ListModelMixin, GenericViewSet):
    queryset = Good.objects.all().order_by('name')
    serializer_class = GoodSerializer
