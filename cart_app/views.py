from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartItemSerializer
from django.shortcuts import get_object_or_404
from product_app.models import Product

class UserCartItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user, active=True)
        items = CartItem.objects.filter(cart=cart).select_related('product')  # Optimization
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)
    
class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user, active=True)
        return cart.items.all()

    def perform_create(self, serializer):
        cart, _ = Cart.objects.get_or_create(user=self.request.user, active=True)
        product_id = self.request.data.get('product_id')  # <- FIXED line
        quantity = int(self.request.data.get('quantity', 1))

        # Validate product
        product = get_object_or_404(Product, id=product_id)

        # Check if item exists
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer.instance = cart_item  # Manual assignment to return created/updated item
class CartItemUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
