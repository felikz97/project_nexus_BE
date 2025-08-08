# category_app/urls.py
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CategoryAdminViewSet

router = DefaultRouter()
router.register(r'', CategoryViewSet, basename='category')  # public categories
router.register(r'admin', CategoryAdminViewSet, basename='admin-categories')  # admin categories

urlpatterns = router.urls
