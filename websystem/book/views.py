from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from websystem.mixins import AdvFlexFieldsMixin

from .models import Book
from .serializers import BookSerializer


# Create your views here.
class BookViewSet(AdvFlexFieldsMixin, ModelViewSet):
    queryset = Book.objects.all().prefetch_related(*Book.PREFETCHED_RELATED_FIELDS)
    serializer_class = BookSerializer
