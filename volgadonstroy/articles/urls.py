from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ArticleReadOnlyModelViewSet, ArticleListView, ArticleDetailView

router = SimpleRouter()
router.register(r'', ArticleReadOnlyModelViewSet)

urlpatterns = [
    path('admin/list/', ArticleListView.as_view(), name='articles-list'),
    path('admin/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]

urlpatterns += router.urls
