from django.urls import path
from .views import (
    UserCartItemsView,
    CartItemListCreateView,
    CartItemUpdateDeleteView,
)

urlpatterns = [
    path('items/', UserCartItemsView.as_view(), name='user-cart-items'),               # GET: list all items in user's cart
    path('items/add/', CartItemListCreateView.as_view(), name='add-cart-item'),        # POST: add new item
    path('items/<int:pk>/', CartItemUpdateDeleteView.as_view(), name='update-cart-item'),  # PUT/PATCH/DELETE
]
