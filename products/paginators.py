from rest_framework.pagination import PageNumberPagination


class ProductsPagination(PageNumberPagination):
    page_size = 2


class BrandsPagination(PageNumberPagination):
    page_size = 5
