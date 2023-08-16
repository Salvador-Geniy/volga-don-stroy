from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (MyTokenObtainPairSerializer, UserRegisterSerializer,
                          UserChangePasswordSerializer, UserUpdateSerializer,
                          UserSerializer)


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer


class UserListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.exclude(is_superuser=True)
    serializer_class = UserSerializer


class UserRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegisterView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UserChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserChangePasswordSerializer


class UserUpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
