import pytest


pytestmark = pytest.mark.django_db


class TestFolderViewSet:

    PATH = '/api/v1/folders/'

    def test_should_create_a_folder(self, api_client):
        data = {
            'name': 'Last summer'
        }
        response = api_client.post(self.PATH, data=data)
        response_data = response.json()
        assert response.status_code == 201
        assert data['name'] == response_data['name']
        assert str(api_client.user.id) == str(response_data['user'])

    def test_should_create_a_folder_with_parent(self, api_client, folder):
        data = {'parent_folder': str(folder.id)}
        response = api_client.post(self.PATH, data=data)
        response_data = response.json()
        assert response.status_code == 201
        assert response_data['name'] == 'Untitled Folder'
        assert response_data['parent_folder'] == str(folder.id)
        assert str(api_client.user.id) == str(response_data['user'])

    def test_should_not_create_a_folder_unlogged(self, api_anonymous_client):
        data = {
            'name': 'Last summer'
        }
        response = api_anonymous_client.post(self.PATH, data=data)
        assert response.status_code == 401

    def test_should_create_a_folder_untitled(self, api_client):
        response = api_client.post(self.PATH)
        response_data = response.json()
        assert response.status_code == 201
        assert response_data['name'] == 'Untitled Folder'
        assert str(api_client.user.id) == str(response_data['user'])

    def test_should_list_my_folders(self, api_client, folder):
        # GIVEN
        folder.user = api_client.user
        folder.save()

        # WHEN
        response = api_client.get(self.PATH)

        # THEN
        response_data = response.json()
        assert response.status_code == 200
        assert response_data[0]['name'] == folder.name
        assert response_data[0]['id'] == str(folder.id)

    def test_should_list_my_folders_empty(self, api_client):
        # WHEN
        response = api_client.get(self.PATH)

        # THEN
        response_data = response.json()
        assert not response_data

    def test_should_not_list_unlogged(self, api_anonymous_client):
        response = api_anonymous_client.get(self.PATH)
        assert response.status_code == 401

    def test_should_retrieve_a_folder(self, api_client, folder):
        # GIVEN
        folder.user = api_client.user
        folder.save()

        # WHEN
        response = api_client.get(self.PATH + str(folder.pk))

        # THEN
        response_data = response.json()
        assert response.status_code == 200
        assert response_data['name'] == folder.name
        assert response_data['id'] == str(folder.id)

    def test_should_not_retrieve_a_folder_unlogged(self, api_anonymous_client, folder):
        # WHEN
        response = api_anonymous_client.get(self.PATH + str(folder.pk))

        # THEN
        assert response.status_code == 401

    def test_should_not_retrieve_someoneelse_folder(
            self, api_client, folder,
            second_user):
        # GIVEN
        folder.user = second_user
        folder.save()

        # WHEN
        response = api_client.get(self.PATH + str(folder.pk))

        # THEN
        assert response.status_code == 403
        assert not response.data
