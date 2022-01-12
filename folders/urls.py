from rest_framework import routers
from folders.views import FolderViewSet


folder_api_router = routers.SimpleRouter(trailing_slash=False)
folder_api_router.register(r'', FolderViewSet, basename='folders-api')


urlpatterns = []
urlpatterns += folder_api_router.urls
