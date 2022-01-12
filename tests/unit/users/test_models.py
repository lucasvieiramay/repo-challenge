import pytest
from django.contrib.auth.models import AbstractUser

from utils.models import BaseModel
from users.models import User


pytestmark = pytest.mark.django_db


class TestUserModel:

    def test_subclass(self):
        assert issubclass(User, BaseModel)
        assert issubclass(User, AbstractUser)

    def test_str(self, user):
        assert str(user) == f'{user.full_name} | {user.pk}'

    @pytest.mark.parametrize(
        ['full_name', 'expected_firstname'],
        [
            ('Lucas Vieira May', 'Lucas'),
            ('Lucas', 'Lucas'),
            ('Rodolfo Pinotti', 'Rodolfo'),
            ('Lucas May', 'Lucas'),
            ('Name Ultra Mega Long Giant', 'Name'),
        ]
    )
    def test_first_name(self, full_name, expected_firstname, user):
        user.full_name = full_name
        user.save()

        assert user.first_name == expected_firstname
