from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views


api_path = settings.API_PATH


urlpatterns = [
    path('admin/', admin.site.urls),
    path(api_path + 'users/', include('users.urls')),
    path(api_path + 'token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(api_path + 'token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
