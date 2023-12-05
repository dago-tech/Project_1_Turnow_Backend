from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from apps.users.permissions import IsAdminUser
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


class UserListAPIView(generics.ListAPIView):
    """
    List of users using GET method
    """
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    #permission_classes = [IsAdminUser]


class UserCreateAPIView(generics.CreateAPIView):
    
    serializer_class = CustomUserSerializer
    #permission_classes = [IsAdminUser]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Retrieve a user using GET method
    """
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    #permission_classes = [IsAdminUser]


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Update a user using PUT method
    """
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    #permission_classes = [IsAdminUser]


class UserDeleteAPIView(generics.DestroyAPIView):
    """
    Delete a user using DELETE method
    """
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    #permission_classes = [IsAdminUser]
