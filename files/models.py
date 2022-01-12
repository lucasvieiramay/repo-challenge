from django.db import models
from utils.models import BaseModel


class File(BaseModel):
    folder = models.ForeignKey('folders.Folder', on_delete=models.CASCADE, related_name='files')
    django_filefield = models.FileField()

    class Meta:
        db_table = 'FILE'

    def __str__(self):
        return f'{self.django_filefield.name} - {self.folder}'

    @property
    def breadcumb(self):
        pass
