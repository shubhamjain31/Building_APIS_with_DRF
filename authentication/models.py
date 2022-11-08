from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

# Create your models here.


class User(AbstractUser):
    email               = models.CharField(max_length=80, unique=True)
    username            = models.CharField(max_length=45)
    date_of_birth       = models.DateField(null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username