from rest_framework.serializers import ModelSerializer

from goods.models import Good


class GoodSerializer(ModelSerializer):
    class Meta:
        model = Good
        fields = '__all__'

