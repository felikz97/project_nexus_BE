from django.db import models

# Create your models here.
from users_app.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=150)

    def __str__(self):
        return self.store_name