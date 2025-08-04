from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]  # Only admin users can access

    def perform_create(self, serializer):
        serializer.save()
