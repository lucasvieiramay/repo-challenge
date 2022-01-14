from folders.views import FolderViewSet

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class TestFolderViewSet:

    def test_parent_class(self):
        assert issubclass(FolderViewSet, ModelViewSet)

    def test_permission_classes(self):
        permission_classes = FolderViewSet.permission_classes
        assert len(permission_classes) == 1
        assert permission_classes[0] == IsAuthenticated
