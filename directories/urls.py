from rest_framework import routers
from directories.views import DirectoryViewSet


directory_api_router = routers.SimpleRouter(trailing_slash=False)
directory_api_router.register(r'', DirectoryViewSet, basename='directory-api')


urlpatterns = []
urlpatterns += directory_api_router.urls
