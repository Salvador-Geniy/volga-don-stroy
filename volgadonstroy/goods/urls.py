from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (CategoriesListCreateAdminView, CategoriesRetrieveUpdateDestroyAdminView,
                    GoodReadOnlyModelViewSet, GoodListAdminView, GoodCreateView, GoodDetailView)

router = SimpleRouter()
router.register(r'', GoodReadOnlyModelViewSet)

urlpatterns = [
    path('admin/categories/', CategoriesListCreateAdminView.as_view(), name='categories-list'),
    path('admin/categories/<int:pk>/', CategoriesRetrieveUpdateDestroyAdminView.as_view(), name='category-detail'),
    path('admin/list/', GoodListAdminView.as_view(), name='good-list'),
    path('admin/add/', GoodCreateView.as_view(), name='add-good'),
    path('admin/<int:pk>/', GoodDetailView.as_view(), name='good-detail')
]

urlpatterns += router.urls
