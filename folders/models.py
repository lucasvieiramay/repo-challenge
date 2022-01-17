from django.db import models
from utils.models import BaseModel


class Folder(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='folders')
    name = models.CharField(max_length=256, db_index=True, default='untitled folder')
    color_hexa = models.CharField(max_length=6, null=True)
    parent_folder = models.ForeignKey(
        'self', null=True, on_delete=models.CASCADE,
        related_name='subfolders')

    class Meta:
        db_table = 'FOLDER'

    def __str__(self):
        return f'{self.name} - {self.user}'
