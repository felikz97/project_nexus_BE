from django.urls import path
from .views import OrderListCreateView, CheckoutView, OrderDetailView, OrderDetailUpdateView

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('place/', CheckoutView.as_view(), name='checkout'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:id>/', OrderDetailUpdateView.as_view(), name='order-detail'), # for cancelling orders
]