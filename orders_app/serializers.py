from rest_framework import serializers
from .models import Order, OrderItem
from product_app.models import Product  # adjust as needed
from product_app.serializers import ProductSerializer  # if it exists

# ✅ Define a simple Product serializer if not already existing
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image']

# ✅ Now inject product detail into each item
class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

# ✅ Finally, order serializer includes detailed items
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'status', 'created_at', 'items']
