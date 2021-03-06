from rest_framework.viewsets import ModelViewSet

from .permissions import IsAdminOrReadOnly
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly, ]

