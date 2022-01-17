from rest_framework import serializers
from folders.models import Folder
from files.serializers import FileReadSerializer


class FolderReadSerializer(serializers.ModelSerializer):
    objects = serializers.SerializerMethodField()

    class Meta:
        model = Folder
        fields = (
            'id', 'name', 'user',
            'color_hexa', 'parent_folder', 'objects'
        )

    @staticmethod
    def get_objects(obj):
        data = {}
        inner_folders = obj.subfolders.all()
        inner_files = obj.files.all()
        data['folders'] = FolderReadSerializer(inner_folders, many=True).data
        data['files'] = FileReadSerializer(inner_files, many=True).data
        return data


class FolderCreateSerializer(serializers.Serializer):
    name = serializers.CharField(default='Untitled Folder')
    parent_folder = serializers.UUIDField(default=None)
