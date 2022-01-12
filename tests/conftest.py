import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from tests.factories import (
    UserFactory,
    FolderFactory,
    FileFactory
)


register(UserFactory, 'user')
register(UserFactory, 'second_user')
register(FolderFactory, 'folder')
register(FileFactory, 'file')


def create_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    client.user = user
    return client


@pytest.fixture
def api_client(user):
    user.terms_of_service_accepted = True
    user.save()
    return create_client(user)


@pytest.fixture
def api_superuser_client(user):
    user.is_superuser = True
    user.is_staff = True
    user.save()
    return create_client(user)


@pytest.fixture
def api_anonymous_client():
    client = APIClient()
    return client
