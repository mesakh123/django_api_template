from django.shortcuts import render
from helpers.jwt_helper import JWTAuthentication
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from websystem.mixins import AdvFlexFieldsMixin
from websystem.permissions import AdminManagerPermission, AdminPermission

from .models import Book
from .serializers import BookSerializer


# Create your views here.
class BookViewSet(AdvFlexFieldsMixin, ModelViewSet):

    queryset = Book.objects.all().prefetch_related(*Book.PREFETCHED_RELATED_FIELDS)
    serializer_class = BookSerializer

    authentication_classes = (JWTAuthentication,)

    # Limit action , accepted settings:
    # create, retrieve, update, partial_update,destroy and list
    public_action = ["list"]
    protected_action = [
        "create",
        "retrieve",
        "update",
        "partial_update",
    ] + public_action
    private_action = ["delete"] + protected_action

    def get_permissions(self):
        if self.action in self.public_action:
            return [
                permissions.AllowAny(),
            ]
        elif self.action in self.protected_action:
            return [AdminManagerPermission()]
        elif self.action in self.private_action:
            return [AdminPermission()]
        return super().get_permissions()
