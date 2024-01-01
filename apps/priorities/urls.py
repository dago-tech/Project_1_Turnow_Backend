from django.urls import path
from .views import *

app_name = "priorities"

urlpatterns = [
    path("", PriorityListAPIView.as_view(), name="priority_list"),
    path("create/", PriorityCreateAPIView.as_view(), name="priority_create"),
    path("update/<int:pk>/", PriorityUpdateAPIView.as_view(), name="priority_update"),
    path("get/<int:pk>/", PriorityRetrieveAPIView.as_view(), name="priority_retrieve"),
    path("delete/<int:pk>/", PriorityDeleteAPIView.as_view(), name="priority_delete"),
]
