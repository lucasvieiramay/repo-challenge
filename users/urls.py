from rest_framework import routers
from users.views import UsersViewSet


user_api_router = routers.SimpleRouter(trailing_slash=False)
user_api_router.register(r'', UsersViewSet, basename='user-api')


urlpatterns = []
urlpatterns += user_api_router.urls
