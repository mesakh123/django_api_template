from rest_framework.permissions import SAFE_METHODS, BasePermission

from websystem.choices import ROLE_CHOICE

from .exceptions import LoginInvalidException


class IsNotAuthenticated(BasePermission):
    """
    Custom permission to only allow admin to create and edit.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return True
        raise LoginInvalidException

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return True
        raise LoginInvalidException


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user:
            return request.user == obj.user
        return False


class AdminPermission(BasePermission):
    message = "Need admin privilege to perform this operation"

    def has_permission(self, request, view):
        return hasattr(request.user, "role") and request.user.role in [
            ROLE_CHOICE.ADMIN
        ]


class AdminEmployeePermission(BasePermission):
    message = "Need admin or employee privilege to perform this operation"

    def has_permission(self, request, view):
        return hasattr(request.user, "role") and request.user.role in [
            ROLE_CHOICE.ADMIN,
            ROLE_CHOICE.EMPLOYEE,
        ]


class AdminManagerPermission(BasePermission):
    message = "Need admin or manager privilege to perform this operation"

    def has_permission(self, request, view):
        return hasattr(request.user, "role") and request.user.role in [
            ROLE_CHOICE.ADMIN,
            ROLE_CHOICE.MANAGER,
        ]


class SelfPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.username == request.user.username or obj.email == request.user.email:
            return True
        return False
