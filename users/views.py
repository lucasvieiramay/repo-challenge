from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from users.serializers import UserSerializer


class UsersViewSet(ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def me(self, request):
        return Response(
            UserSerializer(request.user).data, status=status.HTTP_200_OK)
