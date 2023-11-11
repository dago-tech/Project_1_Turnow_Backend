from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', UserListAPIView.as_view(), name="user_list"),
    path('create/', CustomUserCreate.as_view(), name="user_create"),
    #path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),name='blacklist')
]