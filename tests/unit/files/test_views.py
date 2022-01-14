from files.views import FileViewSet

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class TestFileViewSet:

    def test_parent_class(self):
        assert issubclass(FileViewSet, ModelViewSet)

    def test_permission_classes(self):
        permission_classes = FileViewSet.permission_classes
        assert len(permission_classes) == 1
        assert permission_classes[0] == IsAuthenticated
