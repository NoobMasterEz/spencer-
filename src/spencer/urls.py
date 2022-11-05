from django.urls import include, path, re_path

from .api.utiles import schema_view
from .api.routers import router

from .module.urls import urls_module

urlpatterns = [
    
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
] + urls_module
