from django.urls import path
from .views import UserCartView, CartItemCreateView, CartItemUpdateDeleteView

urlpatterns = [
    path('', UserCartView.as_view(), name='user-cart'),
    path('items/', CartItemCreateView.as_view(), name='cart-item-create'),
    path('items/<int:pk>/', CartItemUpdateDeleteView.as_view(), name='cart-item-detail'),
]
