import pytest


pytestmark = pytest.mark.django_db


class TestUsersApi:

    def test_users_me(self, api_client):
        user = api_client.user
        response = api_client.get("/api/v1/users/me")
        response_data = response.json()
        assert response.status_code == 200
        assert str(user.id) == str(response_data["id"])

    def test_users_me_anonymous(self, api_anonymous_client):
        response = api_anonymous_client.get("/api/v1/users/me")
        assert response.status_code == 401
