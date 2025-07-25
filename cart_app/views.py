from rest_framework import generics, permissions
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

class UserCartView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user, active=True)
        return cart
    
class CartItemCreateView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        cart, _ = Cart.objects.get_or_create(user=self.request.user, active=True)
        serializer.save(cart=cart)
        
class CartItemUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]