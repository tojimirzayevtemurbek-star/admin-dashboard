from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Product
from .serializers import ProductSerializer


class NoPagination(PageNumberPagination):
    page_size = None


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    pagination_class = NoPagination