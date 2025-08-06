from django.db import models

# Create your models here.
from users_app.models import User

class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100)
    store_description = models.TextField(blank=True)
    store_logo = models.ImageField(upload_to='seller_logos/', null=True, blank=True)
    contact = models.CharField(max_length=150)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.store_name
