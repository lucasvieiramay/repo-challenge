from utils.models import BaseModel

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)


class User(BaseModel, AbstractUser):
    USERNAME_FIELD = 'email'
    username = None
    full_name = models.CharField(max_length=256, db_index=True)
    email = models.EmailField(db_index=True, unique=True)
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        db_table = 'USER'

    def __str__(self):
        return f'{self.full_name} | {self.pk}'

    @property
    def first_name(self):
        return next(iter(self.full_name.split(' ')), self.full_name)
