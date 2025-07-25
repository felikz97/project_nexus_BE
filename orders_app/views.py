from rest_framework import generics, permissions, response
from .models import Order, OrderItem
from cart_app.models import Cart, CartItem
from .serializers import OrderSerializer, OrderItemSerializer
from decimal import Decimal

class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
class CheckoutView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user, active=True)
        if not cart or not cart.items.exists():
            return Response({"detail": "Cart is empty."}, status=400)
        items = cart.items.all()
        total_price = sum(item.product.price * item.quantity for item in items)
        order = Order.objects.create(user=request.user, total_price=Decimal(total_price))
        
        for item in items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
            
        cart.active = False
        cart.save()
        items.delete()
        
        serializer = self.get_serializer(order)
        return response(serializer.data, status=201)
        return response({"detail": "Order created successfully."}, status=201)
    