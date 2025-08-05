from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'is_seller', 'is_staff', 'is_superuser')
    list_filter = ('is_seller', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'Full_Name', 'shop_name')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('Full_Name', 'email', 'mobile', 'address', 'image', 'shop_name', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_seller', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_seller', 'is_staff', 'is_superuser')}
        ),
    )
