from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import GoodViewSet, GoodAdminViewSet

router = SimpleRouter()
router.register(r'goods', GoodViewSet)
router.register(r'goods-admin', GoodAdminViewSet)

urlpatterns = []

urlpatterns += router.urls
