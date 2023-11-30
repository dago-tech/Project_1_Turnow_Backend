from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
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

    def perform_create(self, serializer):
        # If personal_id is not in request, none will be assigned, if we do not write 
        # this line could be a "Not existing key" error
        personal_id = self.request.data.get('personal_id', None)

        # Verify if personal_id already exists in db
        if Client.objects.filter(personal_id=personal_id).exists():
            message = {'error': 'This person is already registered.'}
            return Response(message, status=status.HTTP_201_CREATED)

        # If do not exist, create a new CLient register
        serializer.save()


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

