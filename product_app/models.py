# products_app/models.py
from django.db import models
from django.contrib.auth import get_user_model
from category_app.models import Category
import json

User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    sizes = models.JSONField(blank=True, null=True)
    colors = models.JSONField(blank=True, null=True)
    shoe_sizes = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name
    def is_in_stock(self):
        return self.stock > 0