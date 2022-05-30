from django.shortcuts import render
from helpers.jwt_helper import JWTAuthentication
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from websystem.mixins import AdvFlexFieldsMixin
from websystem.permissions import AdminManagerPermission, AdminPermission

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# Create your views here.
class BookViewSet(AdvFlexFieldsMixin, ModelViewSet):

    queryset = Book.objects.all().prefetch_related(*Book.PREFETCHED_RELATED_FIELDS)
    serializer_class = BookSerializer

    # Limit action , accepted settings:
    # create, retrieve, update, partial_update,destroy and list
    public_action = [
        "list",
        "retrieve",
    ]
    authentication_classes = (JWTAuthentication,)
    protected_action = [
        "create",
        "update",
        "partial_update",
    ] + public_action
    private_action = ["destroy"] + protected_action

    def perform_authentication(self, request):
        if self.action in self.public_action:
            self.authentication_classes = []
        else:
            self.authentication_classes = [JWTAuthentication]
        return self.check_permissions(request)


class AuthorViewSet(AdvFlexFieldsMixin, ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = (JWTAuthentication,)

    # Limit action , accepted settings:
    # create, retrieve, update, partial_update,destroy and list
    public_action = [
        "list",
        "retrieve",
    ]
    protected_action = [
        "create",
        "update",
        "partial_update",
    ] + public_action
    private_action = ["destroy"] + protected_action

    def get_permissions(self):
        if self.action in self.public_action:
            self.authentication_classes = []
            return [
                permissions.AllowAny(),
            ]
        elif self.action in self.protected_action:
            self.authentication_classes = (JWTAuthentication,)
            return [AdminManagerPermission()]
        elif self.action in self.private_action:
            self.authentication_classes = (JWTAuthentication,)
            return [AdminPermission()]
        return super().get_permissions()
