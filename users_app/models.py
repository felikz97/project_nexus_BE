
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    Full_Name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    is_seller = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username