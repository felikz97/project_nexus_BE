from django.db import models

# Create your models here.
from category_app.models import Category
from sellers_app.models import Seller

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to='products/')
    description = models.TextField(max_length=350)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey('users_app.User', on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name