from users.views import UsersViewSet

from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated


class TestUsersApi:

    def test_parent_class(self):
        assert issubclass(UsersViewSet, ViewSet)

    def test_permission_classes(self):
        permission_classes = UsersViewSet.permission_classes
        assert len(permission_classes) == 1
        assert permission_classes[0] == IsAuthenticated
