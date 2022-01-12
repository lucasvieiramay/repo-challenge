import pytest

from utils.models import BaseModel
from folders.models import Folder


pytestmark = pytest.mark.django_db


class TestUserModel:

    def test_subclass(self):
        assert issubclass(Folder, BaseModel)

    def test_str(self, folder):
        assert str(folder) == f'{folder.name} - {folder.user}'
