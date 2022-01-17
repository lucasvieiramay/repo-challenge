from rest_framework.status import HTTP_201_CREATED
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

from django.shortcuts import get_object_or_404

from folders.models import Folder
from folders.serializers import FolderCreateSerializer
from folders.serializers import FolderReadSerializer


class FolderViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = FolderReadSerializer

    def create(self, request):
        serializer = FolderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        parent_folder = None
        if serializer.data['parent_folder']:
            parent_folder = get_object_or_404(Folder, pk=serializer.data['parent_folder'])
            if parent_folder.user != request.user:
                return Response(status=HTTP_403_FORBIDDEN)

        folder = Folder.objects.create(
            user=request.user,
            name=serializer.data['name'],
            parent_folder=parent_folder)
        return Response(FolderReadSerializer(folder).data, status=HTTP_201_CREATED)

    def list(self, request):
        queryset = Folder.objects.filter(user=request.user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        folder = get_object_or_404(Folder, pk=pk)
        if folder.user != request.user:
            return Response(status=HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(folder)
        return Response(serializer.data)
