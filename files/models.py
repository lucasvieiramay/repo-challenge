from django.db import models
from utils.models import BaseModel


class File(BaseModel):
    folder = models.ForeignKey('folders.Folder', on_delete=models.CASCADE, related_name='files')
    file_instance = models.FileField()

    class Meta:
        db_table = 'FILE'

    def __str__(self):
        return f'{self.name} - {self.folder}'

    @property
    def breadcumb(self):
        pass
