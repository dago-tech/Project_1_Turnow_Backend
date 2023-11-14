from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView


class UserListAPIView(generics.ListAPIView):
    """
    List of users using GET method
    """
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    
    serializer_class = CustomUserSerializer

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Retrieve a user using GET method
    """
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class UserRetrieveAPIView(generics.UpdateAPIView):
    """
    Update a user using PUT method
    """
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class UserRetrieveAPIView(generics.DestroyAPIView):
    """
    Delete a user using DELETE method
    """
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
