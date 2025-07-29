from rest_framework import viewsets, filters, serializers, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminOrSellerOwner
from .filters import ProductFilter
from rest_framework.exceptions import ValidationError
import logging

logger = logging.getLogger('products')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrSellerOwner]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price']

    def get_queryset(self):
        return super().get_queryset()
    
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
            seller = getattr(self.request.user, 'seller', None)
            if not seller or seller != serializer.instance.seller:
                raise PermissionError("Only the product owner or admin can update this product.")
            product = serializer.save()
            logger.info(f"[UPDATE] '{product.name}' updated by {self.request.user.username}")
        except Exception as e:
            raise serializers.ValidationError({'error': str(e)})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        seller = getattr(self.request.user, 'seller', None)
        if not request.user.is_staff and seller != instance.seller:
            return Response({'error': 'You do not have permission to delete this product.'},
                            status=status.HTTP_403_FORBIDDEN)
        try:
            instance.delete()
            logger.info(f"[DELETE] Product '{instance.name}' deleted by {self.request.user.username}")
        except Exception as e:
            logger.error(f"[DELETE] Error deleting product '{instance.name}': {str(e)}")
            return Response({'error': 'Failed to delete product.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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
