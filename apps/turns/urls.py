from django.urls import path
from .views import *


app_name = 'turns'

urlpatterns = [
    path('', TurnListAPIView.as_view(), name='turn_list'),
    path('create/', TurnCreateAPIView.as_view(), name='turn_create'),
    path('get/', TurnRetrieveAPIView.as_view(), name='turn_retrieve'),
    path('serve/<int:desk_id>/', First_to_serveAPIView.as_view(), name='turn_serve'),
    path('serving/<int:desk_id>/', ServingTurnAPIView.as_view(), name='turn_serving'),
    path('served/<int:desk_id>/', ServedTurnAPIView.as_view(), name='turn_served'),
    path('update/<int:pk>/', TurnUpdateAPIView.as_view(), name='turn_update'),
    path('delete/<int:pk>/', TurnDeleteAPIView.as_view(), name='turn_delete'),
]