from .serializers import *
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.permissions import IsAdminUser


class DeskListAPIView(generics.ListAPIView):
    """
    List of Desks using GET method
    """
    serializer_class = DeskSerializer
    queryset = Desk.objects.all()
    #permission_classes = [IsAdminUser]

class GetDeskAPIView(APIView):
    serializer_class = DeskSerializer

    def get(self, request, *args, **kwargs):
        data = {
            'desk_id': '',
            'desk_name': '',
            'message': ''
        }
        user_id = kwargs['user_id']
        desk = Desk.objects.filter(user=user_id).first()

        if desk is not None:
            data['desk_id'] = desk.id
            data['desk_name'] = desk.name
            data['message'] = 'desk_name'
            return Response(data, status=status.HTTP_200_OK)
        elif desk is None:
            data['message'] = 'empty'
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


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
