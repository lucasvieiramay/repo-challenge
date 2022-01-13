from rest_framework import routers
from files.views import FileViewSet


file_api_router = routers.SimpleRouter(trailing_slash=False)
file_api_router.register(r'', FileViewSet, basename='files-api')


urlpatterns = []
urlpatterns += file_api_router.urls
