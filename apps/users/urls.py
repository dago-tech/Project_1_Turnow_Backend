from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', UserListAPIView.as_view(), name="user_list"),
    path('create/', UserCreateAPIView.as_view(), name="user_create"),
    path('is_admin/<int:user_id>/', IsAdminAPIView.as_view(), name='user_is_admin'),
    path('get_user_email/<int:user_id>/', GetUserEmailAPIView.as_view(), name='user_email'),
    path('get/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name="user_update"),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name="user_delete"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist')
]