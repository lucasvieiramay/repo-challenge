import factory
from files.models import File


class FileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = File

    folder = factory.SubFactory('tests.factories.folders.FolderFactory')
    django_filefield = factory.django.FileField(data='data')
