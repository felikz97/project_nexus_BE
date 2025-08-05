from rest_framework import viewsets, filters, serializers, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminOrSellerOwner
from .filters import ProductFilter
from rest_framework.exceptions import ValidationError
import logging
import django_filters

logger = logging.getLogger('products')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrSellerOwner]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['price']
    ordering = ['id']

    def get_queryset(self):
         return super().get_queryset().order_by('-id')


    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def mine(self, request):
        user_products = self.queryset.filter(seller=request.user)
        page = self.paginate_queryset(user_products)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(user_products, many=True)
        return Response(serializer.data)

    
    def perform_create(self, serializer):
        try:
            product = serializer.save(seller=self.request.user)  # Use correct field name here
            logger.info(
                f"[CREATE] Product '{product.name}' by {self.request.user.username} "
                f"({self.request.user.id}) from IP {self.get_client_ip(self.request)}"
            )
        except Exception as e:
            logger.exception("Error during product creation")
            raise serializers.ValidationError({'error': str(e)})


    def perform_update(self, serializer):
        try:
            user = self.request.user
            if serializer.instance.seller != user and not user.is_staff:
                raise PermissionError("Only the product owner or admin can update this product.")
            product = serializer.save()
            logger.info(f"[UPDATE] '{product.name}' updated by {user.username}")
        except Exception as e:
            raise serializers.ValidationError({'error': str(e)})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if not user.is_staff and instance.seller != user:
            return Response({'error': 'You do not have permission to delete this product.'},
                            status=status.HTTP_403_FORBIDDEN)

        try:
            product_name = instance.name  # capture before deletion
            instance.delete()
            logger.info(f"[DELETE] Product '{product_name}' deleted by {user.username}")
        except Exception as e:
            logger.error(f"[DELETE] Error deleting product: {str(e)}")
            return Response({'error': 'Failed to delete product.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'success': f"Product '{product_name}' deleted."}, status=status.HTTP_204_NO_CONTENT)
        return super().destroy(request, *args, **kwargs)
    
    # This method retrieves the client's IP address from the request headers.
    # It checks for the 'HTTP_X_FORWARDED_FOR' header first, which is commonly used in proxy setups.
    # If that header is not present, it falls back to 'REMOTE_ADDR'.
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
class ProductFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product
        fields = ['category'] 