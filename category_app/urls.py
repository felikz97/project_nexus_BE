# category_app/urls.py
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CategoryAdminViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'admin/categories', CategoryAdminViewSet, basename='admin-categories')
urlpatterns = router.urls
