from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
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

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegisterView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UserChangePasswordView(generics.UpdateAPIView):
    model = User
    serializer_class = UserChangePasswordSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj


class UserUpdateProfileView(generics.UpdateAPIView):
    model = User
    serializer_class = UserUpdateSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj


class CurrentUser(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

