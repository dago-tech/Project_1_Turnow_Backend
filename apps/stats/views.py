from django.db.models import F
from rest_framework import generics
from rest_framework.response import Response
from ..turns.models import Turn
from ..turns.serializers import TurnSerializer


class WaitingTimeByTurnView(generics.ListAPIView):
    serializer_class = TurnSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get("start_date", None)
        end_date = self.request.query_params.get("end_date", None)

        queryset = Turn.objects.filter(created__range=[start_date, end_date])
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        result_dict = {turn.turn_number : turn.waiting_time for turn in queryset}

        return Response(result_dict)
