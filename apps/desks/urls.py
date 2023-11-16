from django.urls import path
from .views import *

app_name = 'desks'

urlpatterns = [
    path('', DeskListAPIView.as_view(), name='desk_list'),
    path('create/', DeskCreateAPIView.as_view(), name='desk_create'),
    path('get/<int:pk>/', DeskRetrieveAPIView.as_view(), name='desk_retrieve'),
    path('update/<int:pk>/', DeskUpdateAPIView.as_view(), name='desk_update'),
    path('delete/<int:pk>/', DeskDeleteAPIView.as_view(), name='desk_delete'),
    
]