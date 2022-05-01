from typing import Optional

from rest_framework.serializers import Serializer
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet

from .filter_backends import AdvFlexFieldsFilterBackend


class AdvFlexFieldsMixin:
    filter_backends = [
        AdvFlexFieldsFilterBackend
    ] + api_settings.DEFAULT_FILTER_BACKENDS


class ActionBasedSerializerClassMixin(ModelViewSet):
    serializer_class: Optional[type[Serializer]] = None
    list_serializer_class: Optional[type[Serializer]] = None
    create_serializer_class: Optional[type[Serializer]] = None
    retrieve_serializer_class: Optional[type[Serializer]] = None
    update_serializer_class: Optional[type[Serializer]] = None
    partial_update_serializer_class: Optional[type[Serializer]] = None
    destroy_serializer_class: Optional[type[Serializer]] = None

    def get_serializer_class(self):
        action_serializer_class_map = {
            "list": self.list_serializer_class,
            "create": self.create_serializer_class,
            "retrieve": self.retrieve_serializer_class,
            "update": self.update_serializer_class,
            "partial_update": self.partial_update_serializer_class,
            "destroy": self.destroy_serializer_class,
        }
        return action_serializer_class_map.get(self.action) or self.serializer_class
