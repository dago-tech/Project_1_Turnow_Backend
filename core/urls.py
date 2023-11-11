from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include("apps.users.urls", namespace='user_api')),
    path('api/turn/', include("apps.turns.urls", namespace='turn_api')),
    path('api/client/', include("apps.clients.urls", namespace='client_api')),
    path('api/category/', include("apps.categories.urls", namespace='category_api')),
    path('api/priority/', include("apps.priorities.urls", namespace='priority_api')),
    path('api/desk/', include("apps.desks.urls", namespace='desk_api')),
]
