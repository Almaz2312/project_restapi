from rest_framework import generics, response, status, views
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from products.models import Product
from .permissions import IsAuthor
from .serializers import FavouriteSerializer
from .models import Favourite


class FavouriteListAPIView(generics.ListAPIView):
    serializer_class = FavouriteSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Favourite.objects.filter(customer=user)
        return queryset


class FavouriteAPIView(views.APIView):

    def post(self, request, format=None):
        data = request.data
        product = data.get('product')
        products = Favourite.objects.filter(product=product, customer=request.user)
        if products:
            return response.Response({"message": "You already have"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = FavouriteSerializer(data=data)
        if serializer.is_valid():
            serializer.save(customer=request.user)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(status=status.HTTP_400_BAD_REQUEST)


class FavouriteDeleteAPIView(generics.DestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = [IsAuthor, ]
