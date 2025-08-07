# users_app/ serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','Full_Name', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_seller'] 

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'Full_Name',
            'is_seller', 'mobile', 'address',
            'image', 'shop_name', 'bio'
        ]
        read_only_fields = ['username', 'email']

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'is_seller', 'is_staff', 'is_superuser',
            'Full_Name', 'mobile', 'address', 'shop_name', 'bio', 'image'
        ]
        read_only_fields = ['id', 'username', 'email']
