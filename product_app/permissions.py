#product_app/permissions.py
from rest_framework.permissions import BasePermission

class IsAdminOrSellerOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS are GET, HEAD, OPTIONS — always allow them
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        # Admins can do anything
        if request.user.is_staff:
            return True
        # Seller (owner of product) can edit/delete
        return hasattr(obj, 'seller') and obj.seller == request.user