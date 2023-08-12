from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CategoryViewSet, GoodReadOnlyModeViewSet, GoodAdminView, \
    GoodCreateView, GoodDetailView

router = SimpleRouter()
router.register(r'', GoodReadOnlyModeViewSet)
router.register(r'admin-goods', GoodAdminView)
router.register(r'admin-categories', CategoryViewSet)

urlpatterns = [
    path('admin-add/', GoodCreateView.as_view(), name='add-good'),
    path('admin/<int:pk>/', GoodDetailView.as_view(), name='good-detail')
]

urlpatterns += router.urls
