from rest_framework.permissions import SAFE_METHODS, BasePermission

from websystem.choices import ROLE_CHOICE


class AdminPermission(BasePermission):
    message = "Need admin privilege to perform this operation"

    def has_permission(self, request, view):
        return request.user.role in [ROLE_CHOICE.ADMIN]


class AdminEmployeePermission(BasePermission):
    message = "Need admin or employee privilege to perform this operation"

    def has_permission(self, request, view):
        print("type ", type(request.user.role))
        for t in [ROLE_CHOICE.ADMIN, ROLE_CHOICE.EMPLOYEE]:
            print(f"{t} ", type(t))
        return request.user.role in [ROLE_CHOICE.ADMIN, ROLE_CHOICE.EMPLOYEE]


class AdminManagerPermission(BasePermission):
    message = "Need admin or manager privilege to perform this operation"

    def has_permission(self, request, view):
        return request.user.role in [ROLE_CHOICE.ADMIN, ROLE_CHOICE.MANAGER]


class SelfPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.username == request.user.username or obj.email == request.user.email:
            return True
        return False
