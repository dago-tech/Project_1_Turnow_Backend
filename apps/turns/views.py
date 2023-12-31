from datetime import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from apps.desks.models import Desk


class TurnListAPIView(generics.ListAPIView):
    """
    List of turns using GET method
    """

    serializer_class = TurnSerializer
    queryset = Turn.objects.all()


class NotificationListView(generics.ListAPIView):
    """
    Filter Turn object by state 'first to serve'
    """

    serializer_class = TurnDeskSerializer

    def get_queryset(self):
        queryset = Turn.objects.filter(state="first to serve")
        return queryset

    # Override list method to customize answer when there is no objects in queryset
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            return Response({"message": "There are no turns to serve"})

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TurnRetrieveAPIView(generics.RetrieveAPIView):
    """
    Retrieve a turn using GET method
    """

    serializer_class = TurnSerializer
    queryset = Turn.objects.all()


class RestartTurnAPIView(generics.UpdateAPIView):
    """
    Updates TurnConfig in order to restart turn_number sequence to 'A000' when the
    following turn is created
    """

    queryset = TurnConfig.objects.all()
    serializer_class = TurnConfigSerializer

    def update(self, request, *args, **kwargs):
        # Get or create the unique instance of TurnConfig
        restart_turn = TurnConfig.get_instance()

        if restart_turn:
            # Activate restart flag
            restart_turn.restart_turn = True
            restart_turn.save()

            return Response(
                {"message": "Restart flag activated"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "Error getting or updating instance"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class TurnCreateAPIView(generics.CreateAPIView):
    """
    Create a turn using POST method
    """

    serializer_class = TurnSerializer

    def generate_turn_number(self):
        # Find the last turn by alphabetical and numerical order
        last_turn = Turn.objects.order_by("-created").first()
        # Initialize variables
        new_turn_letter = "A"
        new_number = "000"

        if last_turn:
            letter = last_turn.turn_number[0]
            number = last_turn.turn_number[1:]

            # Increase the number if necessary
            if int(number) < 999:
                new_number = str(int(number) + 1).zfill(3)

            # Increase the letter if necessary
            if letter < "Z" and int(number) == 999:
                # Letter Increment based on Unicode value
                new_turn_letter = chr(ord(letter) + 1)
            elif letter == "Z" and int(number) == 999:
                new_turn_letter = "A"
            else:
                new_turn_letter = letter

        new_turn_number = f"{new_turn_letter}{new_number}"

        return new_turn_number

    def create(self, request, *args, **kwargs):
        # Copy the QueryDict to a mutable instance
        request_data_copy = request.data.copy()

        turn_config = TurnConfig.get_instance()

        # Verificar si la bandera de reinicio está activa
        restart_turn = turn_config.restart_turn
        if restart_turn:
            request_data_copy["turn_number"] = "A000"
            turn_config.restart_turn = False
            turn_config.save()
        else:
            # Generate turn_number value
            turn_number = self.generate_turn_number()
            request_data_copy["turn_number"] = turn_number

        # Create the Turn object using the modified copy
        serializer = self.get_serializer(data=request_data_copy)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NewTurnsCheckerAPIView(APIView):
    serializer_class = TurnSerializer

    def get(self, request, *args, **kwargs):
        data = {"state": False, "message": ""}

        # Get url parameter
        desk_id = kwargs["desk_id"]
        # Get the register of this desk_id
        current_desk = get_object_or_404(Desk, pk=desk_id)

        # Get categories related to this desk
        desk_categories_list = list(current_desk.category.all())

        categories = []
        # Save in a list the categories related to this desk
        for category in desk_categories_list:
            categories.append(category.id)

        # Get the first turn to be served
        turn = (
            Turn.objects.filter(state="pending", category__in=categories)
            .order_by("-priority", "created")
            .first()
        )

        if turn is not None:
            data["state"] = True
            data["message"] = "There are new turns to serve"
            return Response(data, status=status.HTTP_200_OK)
        elif turn is None:
            data["state"] = False
            data["message"] = "There are not new turns to serve"
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class First_to_serveAPIView(generics.UpdateAPIView):
    """
    When a service desk call for a new turn this function finds the first turn to serve
    based on category, priority and creation time, also updates Turn.state and
    Turn.desk attributes. This HTTP request do not requiere a body message
    """

    serializer_class = TurnSerializer

    def get_highest_priority_turn(self):
        """
        Based on the desk_id sent in URL, it gets its categories and compares to pending
        turns. Gets the first turn to be served ordered by priority and creation time.
        Returns said turn and corresponding desk instance.
        """

        """At the same time Desk.busy=True in desks.views.py"""

        # Get the desk_id of desk that is calling for a new turn
        desk_id = self.kwargs["desk_id"]
        # Get the register of this desk_id
        current_desk = get_object_or_404(Desk, pk=desk_id)

        # Get categories related to this desk
        desk_categories_list = list(current_desk.category.all())

        categories = []
        # Save in a list the categories related to this desk
        for category in desk_categories_list:
            categories.append(category.id)

        # Get the first turn to be served
        turn = (
            Turn.objects.filter(state="pending", category__in=categories)
            .order_by("-priority", "created")
            .first()
        )

        return turn, current_desk

    def update(self, request, *args, **kwargs):
        """Updates desk and state fields of the first turn to be served"""

        turn, desk_id = self.get_highest_priority_turn()

        if turn is not None:
            turn.desk = desk_id
            turn.state = "first to serve"
            turn.save()
            # It is no necessary to validate the serializer because a body message is not received
            serializer = self.serializer_class(turn)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "There are no pending turns to serve"},
                status=status.HTTP_404_NOT_FOUND,
            )


class ServingTurnAPIView(generics.UpdateAPIView):
    """
    When a person comes to the service desk, he will tell the user his turn number and the user
    should enter it to the system, it will be compared to the same turn number that was called
    by this desk. If they are equal turn.state will update to serving and start_time will be
    set to now and waiting_time will be calculated. At that time the user must assist the client.
    A body message should be sent with the turn_number in the HTTP request
    """

    serializer_class = TurnSerializer

    def update(self, request, *args, **kwargs):
        """Updates state field of the first turn to be served"""

        turn_number_in_desk = request.data["turn_number"]

        desk_id = self.kwargs["desk_id"]

        turn = Turn.objects.filter(state="first to serve", desk=desk_id).first()

        if (turn is not None) and (turn.turn_number == turn_number_in_desk):
            # Adjust times to project localtime and calculate the waiting_time
            turn.start_time = timezone.localtime(timezone.now()).time()
            created_time = timezone.localtime(turn.created).time()
            turn.waiting_time = (turn.start_time.hour - created_time.hour) * 60 + (
                turn.start_time.minute - created_time.minute
            )
            turn.state = "serving"
            turn.save()

            serializer = self.serializer_class(turn)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "This turn number is not the first to serve for this service desk"},
                status=status.HTTP_404_NOT_FOUND,
            )


class ServedTurnAPIView(generics.UpdateAPIView):
    """
    When user finishes serving the customer, turn.end_time, turn.duration and turn.state
    will be updated.
    A body message is not required in the HTTP request.
    """

    """At the same time Desk.busy=False in desks.views.py"""

    serializer_class = TurnSerializer

    def update(self, request, *args, **kwargs):
        """Updates state field of the first turn to be served"""

        desk_id = self.kwargs["desk_id"]
        turn = Turn.objects.filter(state="serving", desk=desk_id).first()

        if turn:
            # Adjust times to project localtime, set turn.end_time and calculate turn.duration
            turn.end_time = timezone.localtime(timezone.now()).time()
            # Change time format of start time with strptime in order to be able to be compared
            aux_start_time = datetime.strptime(str(turn.start_time), "%H:%M:%S.%f")
            aux_end_time = datetime.strptime(str(turn.end_time), "%H:%M:%S.%f")
            difference = aux_end_time - aux_start_time
            turn.duration = difference.seconds // 60
            turn.state = "served"
            turn.save()

            serializer = self.serializer_class(turn)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "There are no turns being served"},
                status=status.HTTP_404_NOT_FOUND,
            )


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
