from rest_framework import serializers
from files.models import File


class FileReadSerializer(serializers.ModelSerializer):
    folder = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    extension = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = (
            'id', 'folder', 'name',
            'extension',
        )

    @staticmethod
    def get_folder(obj):
        return obj.folder_name

    @staticmethod
    def get_name(obj):
        return obj.filename

    @staticmethod
    def get_extension(obj):
        return obj.extension


class FileCreateSerializer(serializers.Serializer):
    file = serializers.FileField()
    folder = serializers.UUIDField(default=None)
