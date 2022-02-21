from django.db import models
from django.contrib.auth.models import AbstractUser
class rol(AbstractUser):
    rol = models.CharField(max_length=20)
    class Meta:
        db_table = 'auth_user'
