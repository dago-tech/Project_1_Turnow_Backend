from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from core import consumers


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/user/', include("apps.users.urls", namespace='user_api')),
    path('api/turn/', include("apps.turns.urls", namespace='turn_api')),
    path('api/client/', include("apps.clients.urls", namespace='client_api')),
    path('api/category/', include("apps.categories.urls", namespace='category_api')),
    path('api/priority/', include("apps.priorities.urls", namespace='priority_api')),
    path('api/desk/', include("apps.desks.urls", namespace='desk_api')),
    path('docs/', include_docs_urls(title='Turnow')),
    path('schema', get_schema_view(
        title="BlogAPI",
        description="API for the Turnow Project",
        version="1.0.0"
    ), name='openapi-schema'),
]
