from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=80, verbose_name="password")
    
    def __str__(self):
        return self.username
