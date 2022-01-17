from rest_framework import serializers
from folders.models import Folder


class FolderReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = (
            'id', 'name', 'user',
            'color_hexa', 'parent_folder',
        )


class FolderCreateSerializer(serializers.Serializer):
    name = serializers.CharField(default='Untitled Folder')
    parent_folder = serializers.UUIDField(default=None)
