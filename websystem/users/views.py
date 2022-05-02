from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from helpers.jwt_helper import JWTAuthentication
from rest_framework import generics, mixins, permissions, response, status, viewsets
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from websystem.permissions import (
    AdminEmployeePermission,
    AdminManagerPermission,
    AdminPermission,
    SelfPermission,
)

from .models import User
from .serializers import (
    LoginResponseSerializer,
    LoginSerializer,
    RegisterSerializer,
    UserDetailSerializer,
    UserListSerializer,
)


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    lookup_field = "username"
    permission_classes = permissions.IsAuthenticated
    authentication_classes = (JWTAuthentication,)
    serializer_class = UserDetailSerializer


class UsersListAPIView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated, AdminEmployeePermission)
    authentication_classes = (JWTAuthentication,)
    serializer_class = UserListSerializer


class AuthUserAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        user = request.user
        serializer = UserDetailSerializer(user)
        return response.Response({"user": serializer.data})


class RegisterAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = RegisterSerializer

    @extend_schema(request=RegisterSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = LoginSerializer
    response_serializer_class = LoginResponseSerializer

    @extend_schema(request=LoginSerializer, responses=LoginResponseSerializer)
    def post(self, request):
        account = request.data.get("account", None)
        password = request.data.get("password", None)
        user = authenticate(username=account, password=password)

        if user:
            serializer = self.response_serializer_class(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(
            {"message": "Invalid credentials, try again"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
