from rest_framework import generics, views, response, status
# from rest_framework.exceptions import PermissionDenied, NotAcceptable
from django.db.models import Sum
from rest_framework.response import Response

from .permissions import IsAuthor
from .models import Basket
from .serializers import BasketSerializer


class BasketListAPIView(generics.ListAPIView):
    serializer_class = BasketSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Basket.objects.filter(customer=user)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        dicts = {
            "data": serializer.data,
            "total_sum": queryset.aggregate(Sum('total_price'))
        }
        return Response(dicts)


class BasketApiView(views.APIView):

    def post(self, request, format=None):
        data = request.data
        product = data.get('product')
        products = Basket.objects.filter(product=product, customer=request.user)
        if products:
            return response.Response({"message": "You already have"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = BasketSerializer(data=data)
        if serializer.is_valid():
            serializer.save(customer=request.user)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(status=status.HTTP_400_BAD_REQUEST)


class BasketDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [IsAuthor, ]
