from django.db import models
from utils.models import BaseModel


class File(BaseModel):
    folder = models.ForeignKey(
        'folders.Folder', on_delete=models.CASCADE, related_name='files',
        null=True)
    django_filefield = models.FileField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='files')

    class Meta:
        db_table = 'FILE'

    def __str__(self):
        return f'{self.django_filefield.name} - {self.folder}'

    @property
    def folder_name(self):
        return self.folder.name if self.folder else 'root'

    @property
    def filename(self):
        return self.django_filefield.name

    @property
    def extension(self):
        return '.' + self.django_filefield.name.split('.')[-1]
