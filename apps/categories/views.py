from rest_framework import generics
from .serializers import *

class CategoryListAPIView(generics.ListAPIView):
    """
    List of categories using GET method
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryCreateAPIView(generics.CreateAPIView):
    """
    Create a category using POST method
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    """
    Retrieve a category using PUT method
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryUpdateAPIView(generics.UpdateAPIView):
    """
    Update a category using PUT method
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDeleteAPIView(generics.DestroyAPIView):
    """
    Delete a category using DELETE method
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()