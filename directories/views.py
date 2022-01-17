from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from folders.models import Folder
from folders.serializers import FolderReadSerializer


class DirectoryViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = FolderReadSerializer
    model_class = Folder

    def list(self, request):
        folder_id = request.GET.get('folder')
        if folder_id is None:
            # Root folder
            qs = self.model_class.objects.filter(
                user=request.user, parent_folder=None)
        else:
            parent_folder = get_object_or_404(self.model_class, pk=folder_id)
            if parent_folder.user != request.user:
                return Response(status=HTTP_403_FORBIDDEN)

            qs = self.model_class.objects.filter(
                user=request.user, parent_folder=parent_folder)

        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)
