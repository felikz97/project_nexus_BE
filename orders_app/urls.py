from django.urls import path
from .views import OrderListCreateView, CheckoutView

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]