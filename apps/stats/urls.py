from django.urls import path
from .views import *

app_name = "stats"

urlpatterns = [
    path("waiting_time/", WaitingTimeByTurnView.as_view(), name="waiting_time_turn"),
    path("waiting_time_desk/", WaitingTimeByDeskView.as_view(), name="waiting_time_desk"),
    #path("delete/<int:pk>/", PriorityDeleteAPIView.as_view(), name="priority_delete"),
]