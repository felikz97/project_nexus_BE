from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]

# allow users to reset their password
urlpatterns += [
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(email_template_name='email/password_reset_email.html'), 
        name='password_reset'),
    path(
        'password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
]