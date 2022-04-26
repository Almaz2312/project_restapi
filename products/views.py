from rest_framework import generics, response
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.decorators import action

from .permissions import IsAdminOrReadOnly
from .models import Product, Brand, Image
from .serializers import ProductSerializer, BrandSerializer, ImageSerializer
from .paginators import ProductsPagination, BrandsPagination


class BrandViewSet(ModelViewSet):
    pagination_class = BrandsPagination
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminUser | IsAdminOrReadOnly]


class ProductListAPIView(generics.ListAPIView):
    pagination_class = ProductsPagination
    queryset = Product
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(
                Q(name__icontains=name) | Q(description__icontains=name)
            )
        return queryset
    #
    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     name = self.request.query_params.get('name')
    #     if name:
    #         queryset = queryset.filter(
    #             Q(name__icontains=name) | Q(category__icnotains=name)
    #         )
    #     return queryset


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class ProductDetailDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]


class ImageModelViewSet(ModelViewSet):
    pagination_class = BrandsPagination
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAdminUser | IsAdminOrReadOnly]