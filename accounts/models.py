from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, PermissionsMixin


class CustomUser(AbstractUser):
    email = models.EmailField(blank=True, null=True)

    REQUIRED_FIELDS = []

    class Meta:
        swappable = 'AUTH_USER_MODEL'
