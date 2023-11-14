from rest_framework import generics
from .serializers import *


class ClientListAPIView(generics.ListAPIView):
    """
    List of clients using GET method
    """
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientRetrieveAPIView(generics.RetrieveAPIView):
    """
    Retrieve a client using GET method
    """
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientCreateAPIView(generics.CreateAPIView):
    """
    Create a client using POST method
    """
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientUpdateAPIView(generics.UpdateAPIView):
    """
    Update a client using PUT method
    """
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientDeleteAPIView(generics.DestroyAPIView):
    """
    Delete a client using DELETE method
    """
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

