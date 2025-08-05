# products_app/filters.py
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    categories = django_filters.BaseInFilter(field_name='category', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['categories']
