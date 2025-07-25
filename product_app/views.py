from rest_framework import viewsets, filters
from .models import Product
from .serializers import ProductSerializer
from rest_framework import filters as drf_filters
from .permissions import IsAdminOrSellerOwner
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrSellerOwner]
    
    # Filter, search, and ordering settings
    filtersets_class = ProductFilter
    
    search_fields = ['name', 'description']
    filter_fields = {
        'category',
        'name',
    }
    ordering_fields = ['price']
