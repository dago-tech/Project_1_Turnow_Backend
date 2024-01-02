from django.urls import path
from .views import *

app_name = "clients"

urlpatterns = [
    path("", ClientListAPIView.as_view(), name="client_list"),
    path("create/", ClientCreateAPIView.as_view(), name="client_create"),
    path("get/<int:pk>/", ClientRetrieveAPIView.as_view(), name="client_retrieve"),
    path("update/<int:pk>/", ClientUpdateAPIView.as_view(), name="client_update"),
    path("delete/<int:pk>/", ClientDeleteAPIView.as_view(), name="client_delete"),
]
