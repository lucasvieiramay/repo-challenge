import pytest

from utils.models import BaseModel
from files.models import File


pytestmark = pytest.mark.django_db


class TestFileModel:

    def test_subclass(self):
        assert issubclass(File, BaseModel)

    def test_str(self, file):
        assert str(file) == f'{file.django_filefield.name} - {file.folder}'

    def test_folder_name(self, file):
        folder_name = file.folder.name
        assert file.folder_name == folder_name

    def test_folder_name_without_folder(self, file):
        file.folder = None
        file.save()
        assert file.folder_name == 'root'

    def test_filename(self, file):
        assert file.filename == file.django_filefield.name

    def test_extension(self, file):
        assert file.extension == '.dat'
