from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import FeedbackViewSet, FeedbackCreateView

router = SimpleRouter()

router.register(r'admin', FeedbackViewSet)

urlpatterns = [
    path('add/', FeedbackCreateView.as_view(), name='add-feedback')
]

urlpatterns += router.urls
