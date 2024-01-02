from rest_framework import generics
from .serializers import *


class PriorityListAPIView(generics.ListAPIView):
    """
    List of priorities using GET method
    """

    serializer_class = PrioritySerializer
    queryset = Priority.objects.all()


class PriorityRetrieveAPIView(generics.RetrieveAPIView):
    """
    Retrieve a priority using GET method
    """

    serializer_class = PrioritySerializer
    queryset = Priority.objects.all()


class PriorityCreateAPIView(generics.CreateAPIView):
    """
    Create a priority using POST method
    """

    serializer_class = PrioritySerializer
    queryset = Priority.objects.all()


class PriorityUpdateAPIView(generics.UpdateAPIView):
    """
    Update a priority using PUT method
    """

    serializer_class = PrioritySerializer
    queryset = Priority.objects.all()


class PriorityDeleteAPIView(generics.DestroyAPIView):
    """
    Delete a priority using DELETE method
    """

    serializer_class = PrioritySerializer
    queryset = Priority.objects.all()
