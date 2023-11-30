from .serializers import *
from rest_framework import generics
from apps.users.permissions import IsAdminUser


class DeskListAPIView(generics.ListAPIView):
    """
    List of Desks using GET method
    """
    serializer_class = DeskSerializer
    queryset = Desk.objects.all()
    #permission_classes = [IsAdminUser]


class DeskRetrieveAPIView(generics.RetrieveAPIView):
    """
    Retrieve a Desk using GET method
    """
    serializer_class = DeskSerializer
    queryset = Desk.objects.all()


class DeskCreateAPIView(generics.CreateAPIView):
    """
    Create a Desk using POST method
    """
    serializer_class = DeskSerializer
    queryset = Desk.objects.all()


class DeskUpdateAPIView(generics.UpdateAPIView):
    """
    Update a Desk using PUT method
    """
    serializer_class = DeskSerializer
    queryset = Desk.objects.all()


class DeskDeleteAPIView(generics.DestroyAPIView):
    """
    Delete a Desk using DELETE method
    """
    serializer_class = DeskSerializer
    queryset = Desk.objects.all()
