from datetime import datetime
from django.utils import timezone
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status 


class TurnListAPIView(generics.ListAPIView):
    """
    List of turns using GET method
    """
    serializer_class = TurnSerializer
    queryset = Turn.objects.all()


class TurnRetrieveAPIView(generics.RetrieveAPIView):
    """
    Retrieve a turn using PUT method
    """
    serializer_class = TurnSerializer
    queryset = Turn.objects.all()


class TurnCreateAPIView(generics.CreateAPIView):
    """
    Create a turn using POST method
    """
    serializer_class = TurnSerializer

    def generate_turn_number(self):
        # Find the last turn by alphabetical and numerical order
        last_turn = Turn.objects.order_by('-turn_number').first()
        # Initialize variables
        new_turn_letter = 'A'
        new_number = '000'

        if last_turn:
            letter = last_turn.turn_number[0]
            number = last_turn.turn_number[1:]
            # Increase the letter if necessary
            if letter < 'Z' and int(number)==999:
                new_turn_letter = chr(ord(letter) + 1)
            else:
                new_turn_letter = letter
            # Increase the number if necessary
            if int(number) < 999:
                new_number = str(int(number) + 1).zfill(3)

        new_turn_number = f"{new_turn_letter}{new_number}"

        return new_turn_number
    

    def create(self, request, *args, **kwargs):
        # Copy the QueryDict to a mutable instance
        request_data_copy = request.data.copy()

        # Generate turn_number value
        turn_number = self.generate_turn_number()

        request_data_copy['turn_number'] = turn_number

        # Create the Turn object using the modified copy
        serializer = self.get_serializer(data=request_data_copy)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class start_timeAPIView(APIView):    
    """
    Update start_time field with current date, this HTTP request 
    do not require a body message. Uses PUT method
    """
    
    def put(self, request, pk):
        try:
            queryset = Turn.objects.get(pk=pk)
        except Turn.DoesNotExist:
            return Response({'detail': 'This object do not exist.'}, status=status.HTTP_404_NOT_FOUND)

        queryset.start_time = timezone.localtime(timezone.now()).time()
        queryset.save()

        return Response({'message': 'Date and time updated successfully'}, status=status.HTTP_200_OK)
    

class end_timeAPIView(APIView):    
    """
    Update end_time and duration fields with current date, this HTTP request do 
    not require a body message. Uses PUT method
    """
    
    def put(self, request, pk):
        try:
            queryset = Turn.objects.get(pk=pk)
        except Turn.DoesNotExist:
            return Response({'detail': 'This object do not exist.'}, status=status.HTTP_404_NOT_FOUND)
        if queryset.start_time:
            queryset.end_time = timezone.localtime(timezone.now()).time()
            aux_start_time = datetime.strptime(str(queryset.start_time), '%H:%M:%S.%f')
            aux_end_time = datetime.strptime(str(queryset.end_time), '%H:%M:%S.%f')
            difference = aux_end_time - aux_start_time
            print(difference)
            queryset.duration = (difference.seconds // 60)
            queryset.save()
        else:
            return Response({'detail': 'start_time do not exist in this turn.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Date and time updated successfully'}, status=status.HTTP_200_OK)
    

class First_to_serveView(generics.UpdateAPIView):
    """
    Find the first turn to serve based on priority and creation time
    Update its state attribute
    """
    queryset = Turn.objects.all()
    serializer_class = TurnSerializer

    def get_highest_priority_turn(self):
        turn = Turn.objects.filter(state='pending').order_by('-priority', '-created').first()
        return turn

    def update(self, request, *args, **kwargs):
        turn = self.get_highest_priority_turn()

        if turn:
            turn.state = 'first to serve'
            turn.save()

            serializer = TurnSerializer(turn)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'There are no pending turns to serve'}, status=status.HTTP_204_NO_CONTENT)
        


class TurnUpdateAPIView(generics.UpdateAPIView):
    """
    Update a turn using PUT method
    """
    serializer_class = TurnSerializer
    queryset = Turn.objects.all()


class TurnDeleteAPIView(generics.DestroyAPIView):
    """
    Delete a turn using DELETE method
    """
    serializer_class = TurnSerializer
    queryset = Turn.objects.all()




""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""