from rest_framework import pagination


class AbstractSetPagination(pagination.PageNumberPagination):
    page_size_query_param = "page_size"
    page_query_param = "page"


class SmallResultsSetPagination(AbstractSetPagination):
    page_size = 5


class MediumResultsSetPagination(AbstractSetPagination):
    page_size = 25


class LargeResultsSetPagination(AbstractSetPagination):
    page_size = 50
