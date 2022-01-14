from rest_framework.status import HTTP_201_CREATED
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from folders.models import Folder
from folders.serializers import FolderCreateSerializer
from folders.serializers import FolderReadSerializer


class FolderViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = FolderReadSerializer

    def create(self, request):
        serializer = FolderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # TODO: Receive the parent_folder to bound the folder into a diretory
        folder = Folder.objects.create(
            user=request.user, name=serializer.data['name'])
        return Response(FolderReadSerializer(folder).data, status=HTTP_201_CREATED)

    def list(self, request):
        # TODO: Get only root folders
        queryset = Folder.objects.filter(user=request.user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        pass
