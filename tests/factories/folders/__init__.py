import factory
from folders.models import Folder


class FolderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Folder

    name = factory.Faker("name")
    user = factory.SubFactory('tests.factories.users.UserFactory')
