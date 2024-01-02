from django.urls import path
from .views import *

app_name = "categories"

urlpatterns = [
    path("", CategoryListAPIView.as_view(), name="category_list"),
    path("create/", CategoryCreateAPIView.as_view(), name="category_create"),
    path("get/<int:pk>/", CategoryRetrieveAPIView.as_view(), name="category_retrieve"),
    path("update/<int:pk>/", CategoryUpdateAPIView.as_view(), name="category_update"),
    path("delete/<int:pk>/", CategoryDeleteAPIView.as_view(), name="category_delete"),
]
