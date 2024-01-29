from django.urls import path
from .views import *

app_name = "stats"

urlpatterns = [
    path("waiting_time/", WaitingTimeByTurnView.as_view(), name="waiting_time_turn"),
    path("waiting_time/<str:model>/", WaitingTimeByModelView.as_view(), name="waiting_time_desk"),
    path("turn_count/<str:model>/", TurnCountView.as_view(), name="turn_count"),
]