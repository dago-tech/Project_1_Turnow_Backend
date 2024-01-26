from django.db.models import Avg
from rest_framework import generics, status
from rest_framework.response import Response
from ..turns.models import Turn, Desk
from ..turns.serializers import TurnSerializer
from .serializers import *


class WaitingTimeByTurnView(generics.ListAPIView):
    """
    waiting_time and duration of turns filtered by start and end times
    """
    serializer_class = TurnSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get("start_date", None)
        end_date = self.request.query_params.get("end_date", None)

        queryset = Turn.objects.filter(created__range=[start_date, end_date])
        return queryset

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        # Get the necessary fields
        if queryset:
            result_data = [
                {
                    "turn_number": turn.turn_number,
                    "waiting_time": turn.waiting_time,
                    "duration": turn.duration,
                }
                for turn in queryset
            ]
            return Response(result_data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "No turns found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class WaitingTimeByDeskView(generics.ListAPIView):
    """
    Average of waiting_time and duration by Service Desk
    """
    serializer_class = WaitingTimeByDeskSerializer

    def get_queryset(self):

        start_date = self.request.query_params.get("start_date", None)
        end_date = self.request.query_params.get("end_date", None)

        turn_filtered = Turn.objects.filter(created__range=[start_date, end_date])

        queryset = Desk.objects.annotate(
            waiting_time_avg=Avg('turn__waiting_time'),
            duration_avg=Avg('turn__duration')
        )
        if queryset:
            queryset = queryset.filter(turn__in=turn_filtered)
            return queryset
        else:
            return Response(
                {"message": "No turns or Service desks found"},
                status=status.HTTP_404_NOT_FOUND,
            )