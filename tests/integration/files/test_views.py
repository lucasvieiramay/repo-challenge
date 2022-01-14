import pytest


pytestmark = pytest.mark.django_db


class TestFileViewSet:

    PATH = '/api/v1/files/'

    def _create_file(self):
        fpath = "testfile.txt"
        f = open(fpath, "w")
        f.write("Hello World")
        f.close()
        f = open(fpath, "r")
        return f

    def test_should_create_a_file(self, api_client):
        data = {
            'file': self._create_file()
        }
        response = api_client.post(self.PATH, data=data)

        assert response.status_code == 201
        assert response.data['folder'] == 'root'
        assert response.data['extension'] == '.txt'

    def test_should_create_a_file_inside_folder(self, api_client, folder):
        data = {
            'file': self._create_file(),
            'folder': str(folder.pk)
        }
        response = api_client.post(self.PATH, data=data)

        assert response.status_code == 201
        assert response.data['folder'] == folder.name
        assert response.data['extension'] == '.txt'

    def test_should_not_create_a_file_unlogged(self, api_anonymous_client):
        data = {
            'file': self._create_file()
        }
        response = api_anonymous_client.post(self.PATH, data=data)

        assert response.status_code == 401

    def test_should_list_my_folders(self, api_client, folder):
        pass

    def test_should_list_my_folders_empty(self, api_client):
        pass

    def test_should_not_list_unlogged(self, api_anonymous_client):
        pass
