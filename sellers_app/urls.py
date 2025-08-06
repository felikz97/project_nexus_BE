from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users_app.views import AdminUserViewSet

router = DefaultRouter()
router.register(r'', AdminUserViewSet, basename='seller-admin')  # or use 'sellers' if you prefer

urlpatterns = [
    path('', include(router.urls)),
]