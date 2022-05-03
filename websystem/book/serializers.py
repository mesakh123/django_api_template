from typing import Literal, Sequence, Union

from rest_framework import serializers
from rest_framework.fields import Field, ReadOnlyField

from websystem.serializers import AdvFlexFieldsModelSerializer

from .models import Author, Book

FIELDS = Union[Sequence[str], Literal["__all__"]]


class BookSerializer(AdvFlexFieldsModelSerializer):
    class Meta:
        model = Book
        fields: FIELDS = "__all__"


class AuthorSerializer(AdvFlexFieldsModelSerializer):
    class Meta:
        model = Author
        fields: FIELDS = (
            "first_name",
            "last_name",
            "date_of_birth",
        )
