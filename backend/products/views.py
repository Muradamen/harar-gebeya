from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Product, Category
from .serializers import (
    ProductSerializer,
    CategorySerializer
)


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(
            seller=self.request.user
        )