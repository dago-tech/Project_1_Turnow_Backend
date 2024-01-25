from django.db.models import Avg, FloatField, ExpressionWrapper, F
from django.db.models.functions import Coalesce, Cast
from django.db.models import OuterRef, Subquery
from rest_framework import generics, status
from rest_framework.response import Response
from ..turns.models import Turn, Desk
from ..turns.serializers import TurnSerializer
from .serializers import *


class WaitingTimeByTurnView(generics.ListAPIView):
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
    serializer_class = WaitingTimeByDeskSerializer

    def get_queryset(self):
        # queryset = Desk.objects.annotate(
        #     waiting_time_avg=Coalesce('turn__waiting_time', 0),
        #     duration_avg=Coalesce('turn__duration', 0)
        # )


        queryset = Desk.objects.annotate(
            waiting_time_avg=Avg('turn__waiting_time'),
            duration_avg=Avg('turn__duration')
        )

        return queryset