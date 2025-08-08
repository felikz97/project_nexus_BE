"""
URL configuration for project_nexus_BE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users_app.views import CurrentUserView, AdminUserViewSet, send_password_reset

# -------------------
# Swagger / OpenAPI Setup
# -------------------
schema_view = get_schema_view(
    openapi.Info(
        title="Project Nexus API",
        default_version='v2',
        description="API documentation for Project Nexus: a comprehensive e-commerce product catalog.",
        terms_of_service="This is a terms of service. More details to be committed later.",
        contact=openapi.Contact(email="felikz.kipkemoi@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# -------------------
# Routers
# -------------------
router = DefaultRouter()
router.register(r'admin/users', AdminUserViewSet, basename='admin-users')

# -------------------
# URL Patterns
# -------------------
urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # API Router (viewsets)
    path('api/', include(router.urls)),

    # Users
    path('api/users/', include(('users_app.urls', 'users_app'), namespace='users')),
    path('api/user/me/', CurrentUserView.as_view(), name='current-user'),
    path('api/password-reset/', send_password_reset, name='password-reset'),

    # Authentication
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='jwt-login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('dj_rest_auth.urls')),

    # Products & Categories
    path('api/products/', include(('product_app.urls', 'product_app'), namespace='products')),
    path('api/categories/', include(('category_app.urls', 'category_app'), namespace='categories')),

    # Orders
    path('api/orders/', include(('orders_app.urls', 'orders_app'), namespace='orders')),

    # Cart
    path('api/cart/', include(('cart_app.urls', 'cart_app'), namespace='cart')),

    # Sellers
    path('api/sellers/', include(('sellers_app.urls', 'sellers_app'), namespace='sellers')),

    # Swagger Docs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# -------------------
# Static & Media (Dev only)
# -------------------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

