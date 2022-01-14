from rest_framework.status import HTTP_201_CREATED
from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from folders.models import Folder

from files.models import File
from files.serializers import FileReadSerializer
from files.serializers import FileCreateSerializer


class FileViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = FileReadSerializer

    def create(self, request):
        serializer = FileCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        folder = None
        if request.data.get('folder'):
            folder = get_object_or_404(Folder, pk=request.data.get('folder'))
            if folder.user != request.user:
                return Response(status=HTTP_403_FORBIDDEN)

        file_obj = File.objects.create(
            user=request.user,
            django_filefield=request.data['file'],
            folder=folder
        )

        return Response(
            self.serializer_class(file_obj).data, status=HTTP_201_CREATED)

    def list(self, request):
        queryset = File.objects.filter(user=request.user)
        folder_id = request.GET.get('folder')
        if folder_id:
            queryset = queryset.filter(folder=folder_id)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
