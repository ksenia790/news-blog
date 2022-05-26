from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class User(AbstractUser):
    username = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=80, unique=True)

    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username