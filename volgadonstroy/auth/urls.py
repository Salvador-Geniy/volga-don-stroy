from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (MyTokenObtainPairView, UserRegisterView,
                    UserChangePasswordView, UserUpdateProfileView,
                    UserListView, UserRetrieveDeleteView, CurrentUser)

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='uses-list'),
    path('users/<int:pk>/', UserRetrieveDeleteView.as_view(), name='user-detail'),
    path('change_password/', UserChangePasswordView.as_view(), name='change-password'),
    path('update_username/', UserUpdateProfileView.as_view(), name='update-profile'),
    path('users/me/', CurrentUser.as_view(), name='user-data')
]
