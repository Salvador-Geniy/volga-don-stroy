from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ArticleViewSet

router = SimpleRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = []

urlpatterns += router.urls
