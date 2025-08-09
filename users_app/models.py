from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    Full_Name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    is_seller = models.BooleanField(default=False)
    mobile = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    shop_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username