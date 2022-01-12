import pytest

from utils.models import BaseModel
from files.models import File


pytestmark = pytest.mark.django_db


class TestFileModel:

    def test_subclass(self):
        assert issubclass(File, BaseModel)

    def test_str(self, file):
        assert str(file) == f'{file.django_filefield.name} - {file.folder}'
