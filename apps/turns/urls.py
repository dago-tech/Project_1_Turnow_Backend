from django.urls import path
from .views import *


#from rest_framework.routers import DefaultRouter

app_name = 'turns'

# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls


urlpatterns = [
    path('', TurnListAPIView.as_view(), name='turn_list'),
    path('create/', TurnCreateAPIView.as_view(), name='turn_create'),
    path('get/', TurnRetrieveAPIView.as_view(), name='turn_retrieve'),
    path('serve/', First_to_serveView.as_view(), name='turn_update'),
    path('start_time/<int:pk>/', start_timeAPIView.as_view(), name='turn_start_time'),
    path('end_time/<int:pk>/', end_timeAPIView.as_view(), name='turn_end_time'),
    path('update/<int:pk>/', TurnUpdateAPIView.as_view(), name='turn_update'),
    path('delete/<int:pk>/', TurnDeleteAPIView.as_view(), name='turn_delete'),
    
]