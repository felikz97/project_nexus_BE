# sellers_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users_app.permissions import IsSeller  # you can create this custom permission

class SellerDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsSeller]

    def get(self, request):
        user = request.user
        return Response({
            "shop_name": user.shop_name,
            "products_count": user.products.count(),  # if related_name='products' in Product model
        })
